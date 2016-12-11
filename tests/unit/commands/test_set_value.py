from tests.unit.fixtures import mock_commands_po as mock_po
from selenium.webdriver.common.keys import Keys


def test_set_value_delegates_to_webelement_and_returns_self(mock_po):
    mock_po.clear = lambda: None

    def send_keys(value):
        mock_po.keys_sent = True
    mock_po.webelement.send_keys = send_keys

    assert mock_po.set_value('spam') == mock_po
    assert mock_po.keys_sent == True


def test_set_value_clears_the_page_object_first(mock_po):
    def clear():
        mock_po.value_cleared = True

    mock_po.clear = clear
    mock_po.webelement.send_keys = lambda value: None

    mock_po.set_value('spam')
    assert mock_po.value_cleared == True


def test_set_value_sends_enter_key_if_called_with_press_enter(mock_po):
    mock_po.clear = lambda: None

    def send_keys(value):
        if value == Keys.ENTER:
            mock_po.enter_pressed = True
        else:
            mock_po.enter_pressed = False
    mock_po.webelement.send_keys = send_keys

    mock_po.set_value('spam', press_enter=True)
    assert mock_po.enter_pressed == True

