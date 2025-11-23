import pytest
import sys
import os
import importlib.util
from unittest.mock import MagicMock

def test_memory_class(mocker):
    """Tests the Memory class logic."""
    mocker.patch.dict(os.environ, {
        "GEMINI_API_KEY": "test",
        "INSTANCE_CONNECTION_NAME": "test-instance",
        "DB_USER": "user",
        "DB_PASS": "pass",
        "DB_NAME": "db"
    })
    
    # Mock Libraries
    mock_genai = MagicMock()
    mock_connector = MagicMock()
    mock_sqlalchemy = MagicMock()
    
    # Inject into sys.modules
    sys.modules["google"] = MagicMock()
    sys.modules["google.genai"] = mock_genai
    sys.modules["google.cloud"] = MagicMock()
    sys.modules["google.cloud.sql"] = MagicMock()
    sys.modules["google.cloud.sql.connector"] = mock_connector
    sys.modules["sqlalchemy"] = mock_sqlalchemy
    
    # Configure Mocks
    # Connector.Connector()
    mock_connector.Connector.return_value = MagicMock()
    
    # SQLAlchemy engine
    mock_engine = MagicMock()
    mock_conn = MagicMock()
    mock_sqlalchemy.create_engine.return_value = mock_engine
    mock_engine.connect.return_value.__enter__.return_value = mock_conn
    
    # Load
    module_path = os.path.join(os.path.dirname(__file__), '../agent.py')
    spec = importlib.util.spec_from_file_location("agent_m03", module_path)
    agent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(agent)
    
    # Test
    memory = agent.Memory()
    memory.save("user", "hello")
    
    assert mock_conn.execute.call_count >= 2
