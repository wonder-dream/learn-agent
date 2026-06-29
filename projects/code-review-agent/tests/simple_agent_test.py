from src.simple_agent import review_code
from unittest.mock import patch, MagicMock
import pytest


def test_llm_chat(mocker):
    mock_chat = mocker.patch(
        "src.simple_agent.LLMClient.chat", return_value="mock 成功了"
    )
    result = review_code('print("hello")')

    assert result == "mock 成功了"
    mock_chat.assert_called_once()
