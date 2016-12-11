from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_enabled_returns_self_when_all_is_fine(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, '_locator_value', 'locator')
    mock_po.wait_until = lambda func, func_kwargs={}, timeout=None, error_msg='': True
    assert mock_po.wait_for_enabled() == mock_po

def test_wait_for_enabled_passes_correct_function_to_wait_until(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, '_locator_value', 'locator')
    mock_po.is_enabled_called = False
    def is_enabled(log=False):
        mock_po.is_enabled_called = True
        return True
    mock_po.is_enabled = is_enabled
    mock_po.wait_for_enabled()
    assert mock_po.is_enabled_called == True

