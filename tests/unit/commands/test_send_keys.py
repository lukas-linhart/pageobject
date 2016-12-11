from tests.unit.fixtures import mock_commands_po as mock_po


def test_send_keys_command_passes_correct_value_to_webelement_send_keys(mock_po):
    def send_keys(keys):
        mock_po.sent_keys = keys
    mock_po.webelement.send_keys = send_keys
    some_keys = 'some keys'
    assert mock_po.send_keys(some_keys) == mock_po
    assert mock_po.sent_keys == some_keys


def test_send_keys_command_returns_self(mock_po):
    mock_po.webelement.send_keys = lambda keys: None
    assert mock_po.send_keys('some keys') == mock_po

