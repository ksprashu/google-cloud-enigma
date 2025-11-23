import pytest
import sys
import os
import importlib.util
from unittest.mock import MagicMock

def test_agent_diagnostics(mocker):
    """Tests the diagnostic run (Cloud Run Job mode)."""
    mocker.patch.dict(os.environ, {"GEMINI_API_KEY": "test_key"})
    
    mock_genai = MagicMock()
    sys.modules["google"] = MagicMock()
    sys.modules["google.genai"] = mock_genai
    
    # Load
    module_path = os.path.join(os.path.dirname(__file__), '../agent.py')
    spec = importlib.util.spec_from_file_location("agent_m02", module_path)
    agent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(agent)
    
    # Configure Mock found in agent
    mock_client = agent.genai.Client.return_value
    mock_response = MagicMock()
    mock_response.text = "Diagnostic OK"
    mock_client.models.generate_content.return_value = mock_response
    
    agent.main()
    
    # Verify
    mock_client.models.generate_content.assert_called_once()