# Official Python Runtime
FROM python:3.11-slim

# Work Directory
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code
COPY . .

# Execution
CMD ["python", "agent.py"]
