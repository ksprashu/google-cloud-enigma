import os
import sqlalchemy
from google.cloud.sql.connector import Connector
from google import genai

class Memory:
    def __init__(self):
        self.instance = os.environ.get("INSTANCE_CONNECTION_NAME")
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASS")
        self.db = os.environ.get("DB_NAME")
        self.connector = Connector()
        self.pool = self._connect()
        self._init_db()

    def _connect(self):
        def getconn():
            return self.connector.connect(
                self.instance,
                "pg8000",
                user=self.user,
                password=self.password,
                db=self.db
            )
        return sqlalchemy.create_engine("postgresql+pg8000://", creator=getconn)

    def _init_db(self):
        with self.pool.connect() as conn:
            conn.execute(sqlalchemy.text(
                "CREATE TABLE IF NOT EXISTS history (id SERIAL PRIMARY KEY, role VARCHAR(20), content TEXT)"
            ))
            conn.commit()

    def save(self, role, text):
        with self.pool.connect() as conn:
            conn.execute(sqlalchemy.text(
                "INSERT INTO history (role, content) VALUES (:role, :content)"),
                {"role": role, "content": text}
            )
            conn.commit()

    def load(self):
        history = []
        with self.pool.connect() as conn:
            result = conn.execute(sqlalchemy.text("SELECT role, content FROM history ORDER BY id"))
            for row in result:
                history.append({"role": row[0], "parts": [row[1]]})
        return history

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    memory = Memory()
    
    chat = client.chats.create(model="gemini-1.5-flash", history=memory.load())
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat.send_message(user_input)
        print(f"Agent: {response.text}")
        memory.save("user", user_input)
        memory.save("model", response.text)

if __name__ == "__main__":
    main()
