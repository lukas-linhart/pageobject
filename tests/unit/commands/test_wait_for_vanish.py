from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_vanish_method_uses_wait_until_vanished_method(monkeypatch, mock_po):
    mock_po.wait_until_vanished_called = False
    def wait_until_vanished(timeout=None):
        mock_po.wait_until_vanished_called = True
        return mock_po
    mock_po.wait_until_vanished = wait_until_vanished

    assert mock_po.wait_for_vanish() == mock_po
    assert mock_po.wait_until_vanished_called == True

