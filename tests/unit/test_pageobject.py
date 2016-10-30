from pageobject import PageObject
import pytest


@pytest.fixture
def mock_po():
    class MockPo(PageObject):
        def __init__(self): pass
    return MockPo()

@pytest.fixture
def another_mock_po():
    class AnotherMockPo(PageObject):
        def __init__(self): pass
    return AnotherMockPo()

@pytest.fixture
def yet_another_mock_po():
    class YetAnotherMockPo(PageObject):
        def __init__(self): pass
    return YetAnotherMockPo()


def test_dunder_init_method_calls_register_child_method_of_parent(monkeypatch, mock_po):
    def mock_register_child(self, child):
        self.child_registered = True
    monkeypatch.setattr(mock_po.__class__, '_register_child', mock_register_child)
    po = PageObject('', mock_po)
    assert mock_po.child_registered is True

def test_dunder_init_method_calls_init_children_method(monkeypatch):
    class MockPageObject(PageObject):
        def init_children(self):
            self.children_initialized = True
    po = MockPageObject('', None)
    assert po.children_initialized is True


def test_dunder_bool_method_returns_True_when_is_existing(mock_po):
    mock_po.is_existing = lambda log=False: True
    assert bool(mock_po)

def test_dunder_bool_method_returns_False_when_is_not_existing(mock_po):
    mock_po.is_existing = lambda log=False: False
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


def test_register_child_method_registers_a_child(monkeypatch, mock_po, another_mock_po):
    monkeypatch.setattr(another_mock_po.__class__, 'name', 'child_po')
    mock_po._register_child(another_mock_po)
    assert mock_po.child_po == another_mock_po


def test_children_property_returns_dict(monkeypatch, mock_po):
    monkeypatch.setattr(mock_po.__class__, 'children', dict())
    assert isinstance(mock_po.children, dict)

def test_children_property_returns_correct_children(monkeypatch, mock_po, another_mock_po, yet_another_mock_po):
    root_po = mock_po
    child_po = another_mock_po
    leaf_po = yet_another_mock_po
    child_po.parent = root_po
    child_po.leaf_po = leaf_po
    child_po.not_a_po = 'not a page object'
    assert 'leaf_po' in child_po.children
    assert 'root_po' not in child_po.children
    assert 'not_a_po' not in child_po.children

