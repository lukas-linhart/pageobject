import pytest
from .fixtures import mock_po, mock_po_list


def test_dunder_bool_method_returns_True_if_len_is_nonzero(monkeypatch, mock_po_list):
    monkeypatch.setattr(mock_po_list.__class__, '__len__', lambda self: 1)
    assert bool(mock_po_list)

def test_dunder_bool_method_returns_False_if_len_is_zero(monkeypatch, mock_po_list):
    monkeypatch.setattr(mock_po_list.__class__, '__len__', lambda self: 0)
    assert bool(mock_po_list) == False


def test_dunder_getitem_method_returns_correct_slice(monkeypatch, mock_po_list):
    children = list('spameggs')
    _slice = slice(0, len(children), 2)
    monkeypatch.setattr(mock_po_list.__class__, 'children', children)
    assert mock_po_list[_slice] == children[_slice]


def test_dunder_len_method_returns_children_len(monkeypatch, mock_po_list):
    children = list('spameggs')
    monkeypatch.setattr(mock_po_list.__class__, 'children', children)
    assert len(mock_po_list) == len(children)


def test_get_child_name_returns_correct_name(monkeypatch, mock_po_list):
    index = 2
    class Child:
        def __init__(self):
            self.index = index
    child_po = Child()
    monkeypatch.setattr(mock_po_list.__class__, 'name', 'po_list_name')
    assert mock_po_list._get_child_name(child_po) == '{}[{}]'.format(
            mock_po_list.name, child_po.index)

def test_get_child_full_name_returns_correct_name(monkeypatch, mock_po_list):
    index = 2
    class Child:
        def __init__(self):
            self.index = index
    child_po = Child()
    monkeypatch.setattr(mock_po_list.__class__, 'full_name', 'full_po_list_name')
    assert mock_po_list._get_child_full_name(child_po) == '{}[{}]'.format(
            mock_po_list.full_name, child_po.index)


