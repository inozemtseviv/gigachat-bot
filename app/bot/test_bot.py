import pytest
from unittest.mock import MagicMock, patch

from bot import Bot

@pytest.fixture
def mock_bot(mocker):
    mocker.patch('bot.TeleBot', autospec=True)
    mocker.patch('bot.GigaChat', autospec=True)
    bot_instance = Bot('FAKE_TOKEN', 'FAKE_TOKEN')
    return bot_instance

def test_run_invokes_setup_handlers_and_infinity_polling(mock_bot, mocker):
    mock_bot.setup_handlers = MagicMock()
    mock_bot.bot.infinity_polling = MagicMock()

    mock_bot.run()

    mock_bot.setup_handlers.assert_called_once()
    mock_bot.bot.infinity_polling.assert_called_once()
