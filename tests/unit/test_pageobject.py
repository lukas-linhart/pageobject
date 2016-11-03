import pytest
from pageobject import PageObject
from pageobject.pageobjectbase import PageObjectBase
from .fixtures import mock_po, another_mock_po, yet_another_mock_po


def test_dunder_init_method_assigns_parameters_correctly():
    locator = '//body'
    parent = 'parent_po'
    chain = 'chain'
    webdriver = 'webdriver'
    logger = 'logger'
    name = 'name'
    po = PageObject(locator, parent, chain=chain, webdriver=webdriver, logger=logger, name=name)
    assert po._locator == locator
    assert po.parent == parent
    assert po._chain == chain
    assert po._webdriver == webdriver
    assert po._logger == logger
    assert po._name == name

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


def test_register_child_method_registers_a_child(monkeypatch, mock_po, another_mock_po):
    monkeypatch.setattr(another_mock_po.__class__, 'name', 'child_po')
    mock_po._register_child(another_mock_po)
    assert mock_po.child_po == another_mock_po


def test_get_child_name_returns_correct_name(monkeypatch, mock_po, another_mock_po):
    parent_po = mock_po
    child_po = another_mock_po
    parent_po.child_po = child_po
    child_po_name = 'child_po'
    monkeypatch.setattr(parent_po.__class__, 'children', {child_po_name: child_po})
    assert parent_po._get_child_name(child_po) == child_po_name


def test_get_child_full_name_returns_correct_name(monkeypatch, mock_po, another_mock_po):
    parent_po = mock_po
    child_po = another_mock_po
    parent_full_name = 'parent_full_name'
    monkeypatch.setattr(parent_po.__class__, 'full_name', parent_full_name)
    child_name = 'child_name'
    monkeypatch.setattr(child_po.__class__, 'name', child_name)
    assert parent_po._get_child_full_name(child_po) == '{}{}{}'.format(
            parent_full_name, PageObjectBase.NAME_SEPARATOR, child_name)


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

