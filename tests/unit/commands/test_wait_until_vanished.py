from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_vanish_returns_self_when_all_is_fine(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, '_locator_value', 'locator')
    mock_po.wait_until = lambda func, func_kwargs={}, timeout=None, error_msg='', reverse=None: True
    assert mock_po.wait_for_vanish() == mock_po

def test_wait_for_vanish_passes_correct_function_to_wait_until(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, '_locator_value', 'locator')
    mock_po.is_existing_called = False
    def is_existing(log=False):
        mock_po.is_existing_called = True
        return False
    mock_po.is_existing = is_existing
    mock_po.wait_for_vanish()
    assert mock_po.is_existing_called == True

