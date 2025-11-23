import pytest
import sys
import os
import importlib.util
from unittest.mock import MagicMock

def test_agent_flow(mocker):
    """Tests the chat loop with mocked inputs/API."""
    mocker.patch.dict(os.environ, {"GEMINI_API_KEY": "test_key"})
    
    # Mock Interceptor
    mock_genai = MagicMock()
    sys.modules["google"] = MagicMock()
    sys.modules["google.genai"] = mock_genai
    
    mocker.patch('builtins.input', side_effect=["Hello", "exit"])
    mocker.patch('builtins.print') 
    
    # Load
    module_path = os.path.join(os.path.dirname(__file__), '../agent.py')
    spec = importlib.util.spec_from_file_location("agent_m01", module_path)
    agent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(agent)
    
    # Access the mock used by the agent
    agent_genai = agent.genai
    mock_chat = agent_genai.Client.return_value.chats.create.return_value
    
    # Run
    try:
        agent.main()
    except StopIteration:
        pass
    
    # Verify
    assert mock_chat.send_message.called