from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_visible_method_uses_wait_until_displayed_method(monkeypatch, mock_po):
    mock_po.wait_until_displayed_called = False
    def wait_until_displayed(timeout=None):
        mock_po.wait_until_displayed_called = True
        return mock_po
    mock_po.wait_until_displayed = wait_until_displayed

    assert mock_po.wait_for_visible() == mock_po
    assert mock_po.wait_until_displayed_called == True

