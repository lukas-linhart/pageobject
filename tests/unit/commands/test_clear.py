from tests.unit.fixtures import mock_commands_po as mock_po
from selenium.webdriver.common.keys import Keys


def test_clear_method_delegates_to_webelement_and_returns_self(mock_po):
    mock_po.webelement.clear = lambda: None
    assert mock_po.clear() == mock_po


def test_clear_method_does_not_invoke_pressing_enter_when_false(mock_po):
    mock_po.webelement.clear = lambda: None
    mock_po.enter_pressed = False
    def send_keys(key):
        mock_po.enter_pressed = True
    mock_po.webelement.send_keys = send_keys
    mock_po.clear(press_enter=False)
    assert mock_po.enter_pressed == False


def test_clear_method_delegates_to_webelement_send_keys_if_press_enter(mock_po):
    mock_po.webelement.clear = lambda: None
    def send_keys(key):
        if key == Keys.ENTER:
            mock_po.enter_pressed = True
    mock_po.webelement.send_keys = send_keys
    mock_po.clear(press_enter=True)
    assert mock_po.enter_pressed == True

