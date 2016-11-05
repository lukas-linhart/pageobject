import pytest
from pageobject import PageObject, PageObjectList
from .fixtures import mock_po, mock_po_list


def test_dunder_init_method_assigns_parameters_correctly():
    locator = 1
    parent = 2
    chain = 3
    name = 4
    children_class = 5
    children_locator = 6
    count_locator = 7
    po_list = PageObjectList(locator, parent, chain=chain, name=name,
            children_class=children_class, children_locator=children_locator,
            count_locator=count_locator)
    assert po_list._locator == locator
    assert po_list.parent == parent
    assert po_list._chain == chain
    assert po_list._name == name
    assert po_list._children_class == children_class
    assert po_list._children_locator == children_locator
    assert po_list._count_locator == count_locator

def test_dunder_init_method_calls_register_child_method_of_parent(monkeypatch, mock_po):
    def mock_register_child(self, child):
        self.child_registered = True
    monkeypatch.setattr(mock_po.__class__, '_register_child', mock_register_child)
    po_list = PageObjectList('', mock_po)
    assert mock_po.child_registered


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


def test_children_count_property_returns_a_number(monkeypatch, mock_po_list):
    elements = list('elements')
    class MockWebDriver:
        def find_elements_by_xpath(self, dummy):
            return elements
    monkeypatch.setattr(mock_po_list.__class__, 'count_locator', None)
    monkeypatch.setattr(mock_po_list.__class__, 'webdriver', MockWebDriver())
    assert isinstance(mock_po_list._children_count, int)


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


def test_children_class_property_returns_correct_value_if_initialized(mock_po_list):
    mock_po_list._children_class = 'children_class'
    assert mock_po_list.children_class == mock_po_list._children_class

def test_children_class_property_returns_PageObject_if_not_initialized(mock_po_list):
    mock_po_list._children_class = None
    assert mock_po_list.children_class == PageObject


def test_default_children_locator_returns_None_when_not_provided():
    po_list = PageObjectList('', None)
    assert po_list.default_children_locator == None


def test_children_locator_returns_default_children_locator_if_provided(monkeypatch, mock_po_list):
    monkeypatch.setattr(mock_po_list.__class__, 'default_children_locator', 'default')
    assert mock_po_list.children_locator == mock_po_list.default_children_locator

def test_children_locator_returns_initialized_value_if_provided(monkeypatch, mock_po_list):
    mock_po_list._children_locator = 'children_locator'
    assert mock_po_list.children_locator == mock_po_list._children_locator

def test_children_locator_returns_correct_value_if_not_initialized(monkeypatch, mock_po_list):
    mock_po_list._children_locator = None
    monkeypatch.setattr(mock_po_list.__class__, 'locator', 'locator')
    assert mock_po_list.children_locator == '({})[{}]'.format(mock_po_list.locator, '{}')


def test_default_count_locator_returns_None_when_not_provided():
    po_list = PageObjectList('', None)
    assert po_list.default_count_locator == None

