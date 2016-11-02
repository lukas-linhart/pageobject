import pytest
from .fixtures import mock_po_list


def test_get_child_name_returns_correct_name(monkeypatch, mock_po_list):
    index = 2
    class Child:
        def __init__(self):
            self.index = index
    child_po = Child()
    monkeypatch.setattr(mock_po_list.__class__, 'name', 'po_list')
    assert mock_po_list._get_child_name(child_po) == '{}[{}]'.format(
            mock_po_list.name, child_po.index)

