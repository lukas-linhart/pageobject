from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_enabled_method_uses_wait_until_enabled_method(monkeypatch, mock_po):
    mock_po.wait_until_enabled_called = False
    def wait_until_enabled(timeout=None):
        mock_po.wait_until_enabled_called = True
        return mock_po
    mock_po.wait_until_enabled = wait_until_enabled

    assert mock_po.wait_for_enabled() == mock_po
    assert mock_po.wait_until_enabled_called == True

