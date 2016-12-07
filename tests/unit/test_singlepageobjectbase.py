import pytest
from pageobject import PageObject
from pageobject.singlepageobjectbase import SinglePageObjectBase


class MockPoTemplate(PageObject):
    def __init__(self): pass

@pytest.fixture
def mock_po():
    class MockPo(MockPoTemplate): pass
    return MockPo()


def test_dunder_bool_method_returns_True_when_is_existing(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'is_existing', lambda self, log=False: True)
    assert bool(mock_po) == True

def test_dunder_bool_method_returns_False_when_is_not_existing(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'is_existing', lambda self, log=False: False)
    assert bool(mock_po) == False


def test_dunder_getitem_method_raises_KeyError_for_nonexisting_child(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'children', dict())
    with pytest.raises(KeyError):
        mock_po['nonexisting_child']

def test_dunder_getitem_method_returns_correct_child(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'children', dict(child_po_name='child_po'))
    assert mock_po['child_po_name'] == 'child_po'


def test_dunder_len_method_returns_correct_length(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'children', dict(a=1, b=2))
    assert len(mock_po) == len(mock_po.children)


def test_children_property_returns_dict(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'children', dict())
    assert isinstance(mock_po.children, dict)

def test_children_property_returns_correct_children():
    class MockPo(SinglePageObjectBase): pass
    root_po, child_po, leaf_po = (MockPo() for x in range(3))
    root_po.child_po = child_po
    child_po.leaf_po = leaf_po
    child_po.not_a_po = 'not a page object'
    assert 'leaf_po' in child_po.children
    assert 'root_po' not in child_po.children
    assert 'not_a_po' not in child_po.children


def test_get_child_name_returns_correct_name(monkeypatch, mock_po):
    parent_po = mock_po
    class ChildPo:
        name = 'child_po'
    child_po = ChildPo()
    parent_po.child_po = child_po
    child_po_name = 'child_po'
    monkeypatch.setattr(parent_po.__class__, 'children', {child_po_name: child_po})
    assert parent_po._get_child_name(child_po) == child_po_name


def test_get_child_full_name_returns_correct_name(monkeypatch, mock_po):
    parent_po = mock_po
    class ChildPo:
        name = 'child_name'
    child_po = ChildPo()
    parent_full_name = 'parent_full_name'
    monkeypatch.setattr(parent_po.__class__, 'full_name', parent_full_name)
    child_name = 'child_name'
    monkeypatch.setattr(child_po.__class__, 'name', child_name)
    assert parent_po._get_child_full_name(child_po) == '{}{}{}'.format(
            parent_full_name, parent_po.NAME_SEPARATOR, child_name)


def test_descendants_returns_correct_value(monkeypatch, mock_po):
    class ChildPo(SinglePageObjectBase): pass
    child_po = ChildPo()
    mock_po.child_po = child_po
    class ChildPoList:
        _descendants = None
    child_po_list = ChildPoList()
    mock_po.child_po_list = child_po_list
    children = {'child_po': mock_po.child_po, 'child_po_list': mock_po.child_po_list}
    monkeypatch.setattr(mock_po.__class__, 'children', children)
    descendants = {child_po.name: child_po._descendants, 'child_po_list[i]': None}
    assert mock_po._descendants == descendants

