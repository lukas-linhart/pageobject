from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_interactive_method_uses_wait_until_interactive_method(monkeypatch, mock_po):
    mock_po.wait_until_interactive_called = False
    def wait_until_interactive(timeout=None):
        mock_po.wait_until_interactive_called = True
        return mock_po
    mock_po.wait_until_interactive = wait_until_interactive

    assert mock_po.wait_for_interactive() == mock_po
    assert mock_po.wait_until_interactive_called == True

