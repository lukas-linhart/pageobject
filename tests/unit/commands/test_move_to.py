from tests.unit.fixtures import mock_commands_po as mock_po
from selenium.webdriver.common.action_chains import ActionChains


def test_move_to_command_returns_self(monkeypatch, mock_po):
    mock_webdriver = lambda: None
    monkeypatch.setattr(mock_po.__class__, 'webdriver', mock_webdriver)

    def perform(self):
        pass
    ActionChains.perform = perform

    assert mock_po.move_to() == mock_po


def test_move_to_command_calls_correct_action_chains_method(monkeypatch, mock_po):
    mock_webdriver = lambda: None
    monkeypatch.setattr(mock_po.__class__, 'webdriver', mock_webdriver)

    def move_to_element(self, element):
        mock_po.move_to_element_called = True
        return self
    ActionChains.move_to_element = move_to_element

    def perform(self):
        pass
    ActionChains.perform = perform

    mock_po.move_to()
    assert mock_po.move_to_element_called == True

