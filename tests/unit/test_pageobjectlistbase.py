import pytest
from pageobject.pageobjectlistbase import PageObjectListBase


class MockPoListBase(PageObjectListBase):
    def __init__(self): pass

@pytest.fixture
def mock_po_list_base():
    return MockPoListBase()


def test_dunder_bool_method_returns_True_if_len_is_nonzero(monkeypatch, mock_po_list_base):
    monkeypatch.setattr(mock_po_list_base.__class__, '__len__', lambda self: 1)
    assert bool(mock_po_list_base)

def test_dunder_bool_method_returns_False_if_len_is_zero(monkeypatch, mock_po_list_base):
    monkeypatch.setattr(mock_po_list_base.__class__, '__len__', lambda self: 0)
    assert bool(mock_po_list_base) == False


def test_dunder_getitem_method_returns_correct_slice(monkeypatch, mock_po_list_base):
    children = list('spameggs')
    _slice = slice(0, len(children), 2)
    mock_po_list_base.children = children
    assert mock_po_list_base[_slice] == children[_slice]


def test_dunder_len_method_returns_children_len(monkeypatch, mock_po_list_base):
    children = list('spameggs')
    mock_po_list_base.children = children
    assert len(mock_po_list_base) == len(children)


def test_get_child_name_returns_correct_name(monkeypatch, mock_po_list_base):
    index = 2
    class Child:
        def __init__(self):
            self.index = index
    child_po = Child()
    monkeypatch.setattr(mock_po_list_base.__class__, 'name', 'po_list_name')
    assert mock_po_list_base._get_child_name(child_po) == '{}[{}]'.format(
            mock_po_list_base.name, child_po.index)

def test_get_child_full_name_returns_correct_name(monkeypatch, mock_po_list_base):
    index = 2
    class Child:
        def __init__(self):
            self.index = index
    child_po = Child()
    monkeypatch.setattr(mock_po_list_base.__class__, 'full_name', 'full_po_list_name')
    assert mock_po_list_base._get_child_full_name(child_po) == '{}[{}]'.format(
            mock_po_list_base.full_name, child_po.index)


def test_descendants_returns_descendants_of_children_class_instance(monkeypatch, mock_po_list_base):
    descendants = 'descendants'
    class MockChildrenClass:
        def __init__(self, dummy): pass
        _descendants = descendants
    mock_po_list_base.children_class = MockChildrenClass
    assert mock_po_list_base._descendants == descendants

