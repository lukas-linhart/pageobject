from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_exist_method_uses_wait_until_existing_method(monkeypatch, mock_po):
    mock_po.wait_until_existing_called = False
    def wait_until_existing(timeout=None):
        mock_po.wait_until_existing_called = True
        return mock_po
    mock_po.wait_until_existing = wait_until_existing

    assert mock_po.wait_for_exist() == mock_po
    assert mock_po.wait_until_existing_called == True

