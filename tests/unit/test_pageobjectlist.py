import pytest
from pageobject import PageObject, PageObjectList
from .fixtures import mock_po, mock_po_list


def test_constructor_inits_parameters_correctly():
    locator = 1
    chain = 3
    name = 4
    children_class = 5
    children_locator = 6
    count_locator = 7
    po_list = PageObjectList(locator, chain=chain,
            children_class=children_class, children_locator=children_locator,
            count_locator=count_locator)
    assert po_list._initialized_locator == locator
    assert po_list.parent == None
    assert po_list._chain == chain
    assert po_list._children_class == children_class
    assert po_list._children_locator == children_locator
    assert po_list._initialized_count_locator == count_locator


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


def test_children_count_property_returns_an_int(monkeypatch, mock_po_list):
    elements = list('elements')
    class MockWebDriver:
        def find_elements_by_xpath(self, dummy):
            return elements
    monkeypatch.setattr(mock_po_list.__class__, '_count_locator_value', None)
    monkeypatch.setattr(mock_po_list.__class__, 'webdriver', MockWebDriver())
    assert isinstance(mock_po_list._children_count, int)


def test_children_property_returns_an_empty_list_if_children_count_is_zero(monkeypatch, mock_po_list):
    monkeypatch.setattr(mock_po_list.__class__, 'children_class', None)
    monkeypatch.setattr(mock_po_list.__class__, '_children_count', 0)
    assert mock_po_list.children == []

def test_children_property_returns_instances_of_children_class(monkeypatch, mock_po_list):
    monkeypatch.setattr(mock_po_list.__class__, 'children_class', PageObject)
    monkeypatch.setattr(mock_po_list.__class__, '_children_count', 1)
    monkeypatch.setattr(mock_po_list.__class__, 'children_locator', 'locator')
    assert isinstance(mock_po_list.children[0], mock_po_list.children_class)

def test_children_property_inits_children_with_correct_locator_and_index(monkeypatch, mock_po_list):
    class MockPageObject:
        def __init__(self, locator, chain=True):
            self.test_locator = locator
    children_count = 2
    locator = 'locator[{}]'
    monkeypatch.setattr(mock_po_list.__class__, 'children_class', MockPageObject)
    monkeypatch.setattr(mock_po_list.__class__, '_children_count', children_count)
    monkeypatch.setattr(mock_po_list.__class__, 'children_locator', locator)
    for i in range(children_count):
        assert mock_po_list.children[i].test_locator == locator.format(i+1)
        assert mock_po_list.children[i].index == i


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


def test_provided_children_locator_returns_default_children_locator_when_provided(monkeypatch, mock_po_list):
    default_children_locator = "//default"
    monkeypatch.setattr(mock_po_list.__class__, 'default_children_locator', default_children_locator)
    assert mock_po_list._provided_children_locator == default_children_locator

def test_provided_children_locator_returns_initialized_children_locator_when_default_not_provided(monkeypatch, mock_po_list):
    initialized_children_locator = "//initialized"
    monkeypatch.setattr(mock_po_list.__class__, 'default_children_locator', None)
    mock_po_list._initialized_children_locator = initialized_children_locator
    assert mock_po_list._provided_children_locator == initialized_children_locator

def test_provided_children_locator_returns_correct_value_if_not_initialized(monkeypatch, mock_po_list):
    initialized_locator = "//initialized"
    monkeypatch.setattr(mock_po_list.__class__, 'default_children_locator', None)
    mock_po_list._initialized_children_locator = None
    mock_po_list._initialized_locator = initialized_locator
    assert mock_po_list._provided_children_locator == '({})[{}]'.format(
        mock_po_list._initialized_locator, '{}')


def test_children_locator_returns_default_children_locator_if_provided(monkeypatch, mock_po_list):
    monkeypatch.setattr(mock_po_list.__class__, 'default_children_locator', 'default')
    assert mock_po_list.children_locator == mock_po_list.default_children_locator

def test_children_locator_returns_initialized_value_if_provided(mock_po_list):
    mock_po_list._children_locator = 'children_locator'
    assert mock_po_list.children_locator == mock_po_list._children_locator

def test_children_locator_returns_correct_value_if_not_initialized(monkeypatch, mock_po_list):
    mock_po_list._children_locator = None
    monkeypatch.setattr(mock_po_list.__class__, '_locator_value', 'locator')
    assert mock_po_list.children_locator == '({})[{}]'.format(mock_po_list._locator_value, '{}')


def test_default_count_locator_returns_None_when_not_provided():
    po_list = PageObjectList('', None)
    assert po_list.default_count_locator == None


def test_provided_count_locator_returns_default_count_locator_when_provided(monkeypatch, mock_po_list):
    default_locator = "//default"
    monkeypatch.setattr(mock_po_list.__class__, 'default_count_locator', default_locator)
    assert mock_po_list._provided_count_locator == default_locator

def test_provided_count_locator_returns_initialized_count_locator_when_provided(mock_po_list):
    count_locator = "//count"
    mock_po_list._initialized_count_locator = count_locator
    assert mock_po_list._provided_count_locator == count_locator

def test_provided_count_locator_returns_initialized_locator_as_fallback(mock_po_list):
    locator = "//locator"
    mock_po_list._initialized_count_locator = None
    mock_po_list._initialized_locator = locator
    assert mock_po_list._provided_count_locator == locator


def test_count_locator_inits_locator_with_correct_parameters(monkeypatch, mock_po_list):
    provided_count_locator = "//provided"
    class MockLocator:
        def __init__(self, value, page_object=None):
            self.value = value
            self.page_object = page_object
    monkeypatch.setattr(mock_po_list.__class__, '_locator_class', MockLocator)
    monkeypatch.setattr(mock_po_list.__class__, '_provided_count_locator', provided_count_locator)
    count_locator = mock_po_list._count_locator
    assert count_locator.value == provided_count_locator
    assert count_locator.page_object == mock_po_list


def test_count_locator_value_returns_correct_attribute_of_locator(monkeypatch, mock_po_list):
    count_locator_value = "//body"
    class MockLocator:
        value = count_locator_value
    monkeypatch.setattr(mock_po_list.__class__, '_count_locator', MockLocator)
    assert mock_po_list._count_locator_value == count_locator_value

