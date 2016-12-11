from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_interactive_returns_self_when_all_is_fine(monkeypatch, mock_po):
    mock_po.wait_until = lambda func, func_kwargs={}, timeout=None, error_msg='': True
    assert mock_po.wait_for_interactive() == mock_po

def test_wait_for_interactive_passes_correct_function_to_wait_until(monkeypatch, mock_po):
    mock_po.is_interactive_called = False
    def is_interactive(log=False):
        mock_po.is_interactive_called = True
        return True
    mock_po.is_interactive = is_interactive
    mock_po.wait_for_interactive()
    assert mock_po.is_interactive_called == True

