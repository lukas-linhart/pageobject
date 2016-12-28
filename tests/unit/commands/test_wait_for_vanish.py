from tests.unit.fixtures import mock_commands_po as mock_po


def test_wait_for_vanish_method_uses_wait_until_vanished_method(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'wait_until_vanished', lambda self, timeout=None: self)
    assert mock_po.wait_for_vanish() == mock_po

