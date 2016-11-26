import pytest
import logging
from pageobject import PageObject
from pageobject.pageobjectbase import PageObjectBase
from pageobject.locator import Locator
from .fixtures import mock_po_base
from selenium.webdriver import Remote as RemoteWebDriver


def test_dunder_repr_returns_correct_string(monkeypatch, mock_po_base):
    full_po_name = 'full PO name'
    monkeypatch.setattr(mock_po_base.__class__, 'full_name', full_po_name)
    assert repr(mock_po_base) == '<MockPoBase(MockPoBaseTemplate) (full_name="{}")>'.format(
            mock_po_base.full_name)


def test_default_locator_returns_None_when_not_provided():
    po = PageObjectBase()
    assert po.default_locator is None


def test_parent_locator_returns_correct_value_when_parent_is_valid(monkeypatch, mock_po_base):
    parent_locator = '//body'
    class Parent:
        _locator = parent_locator
    monkeypatch.setattr(mock_po_base.__class__, 'parent', Parent())
    assert mock_po_base._parent_locator == parent_locator

def test_parent_locator_returns_None_when_parent_is_invalid(monkeypatch, mock_po_base):
    monkeypatch.setattr(mock_po_base.__class__, 'parent', None)
    assert mock_po_base._parent_locator == None


def test_locator_inits_Locator_with_default_when_existing(monkeypatch, mock_po_base):
    locator_str = '//body'
    class MockLocator:
        def __init__(self, value, page_object=None):
            self.value = value
            self.page_object = page_object
    monkeypatch.setattr(mock_po_base.__class__, '_locator_class', MockLocator)
    monkeypatch.setattr(mock_po_base.__class__, 'default_locator', locator_str)
    locator = mock_po_base._locator
    assert locator.value == locator_str
    assert locator.page_object == mock_po_base

def test_locator_returns_instantiated_value_when_default_not_provided(monkeypatch, mock_po_base):
    locator_str = '//body'
    class MockLocator:
        def __init__(self, value, page_object=None):
            self.value = value
            self.page_object = page_object
    monkeypatch.setattr(mock_po_base.__class__, '_locator_class', MockLocator)
    monkeypatch.setattr(mock_po_base.__class__, 'default_locator', None)
    mock_po_base._initialized_locator = locator_str
    locator = mock_po_base._locator
    assert locator.value == locator_str
    assert locator.page_object == mock_po_base


def test_webdriver_returns_webdriver_of_a_parent_if_available(monkeypatch, mock_po_base):
    parent_webdriver = 'parent_webdriver'
    class Parent:
        webdriver = parent_webdriver
    monkeypatch.setattr(mock_po_base.__class__, 'parent', Parent())
    assert mock_po_base.webdriver == parent_webdriver

def test_webdriver_returns_correct_value_if_valid(monkeypatch, mock_po_base):
    class MockWebDriver(RemoteWebDriver):
        def __init__(self):  pass
        def __repr__(self): return 'MockWebDriver'
    monkeypatch.setattr(mock_po_base.__class__, 'parent', None)
    mock_po_base._webdriver = MockWebDriver()
    assert mock_po_base.webdriver == mock_po_base._webdriver

def test_webdriver_raises_AssertionException_when_invalid(monkeypatch, mock_po_base):
    monkeypatch.setattr(mock_po_base.__class__, 'parent', None)
    mock_po_base._webdriver = None
    with pytest.raises(AssertionError):
        mock_po_base.webdriver


def test_logger_returns_standard_logging(mock_po_base):
    mock_po_base._logger = None
    assert mock_po_base.logger == logging


def test_name_returns_initialized_value_if_valid(mock_po_base):
    mock_po_base._name = 'valid name'
    assert mock_po_base.name == mock_po_base._name

def test_name_returns_correct_name_when_parent_exists(monkeypatch, mock_po_base):
    correct_name = 'child_name'
    class Parent:
        def _get_child_name(self, child): return correct_name
    mock_po_base._name = None
    monkeypatch.setattr(mock_po_base.__class__, 'parent', Parent())
    assert mock_po_base.name == correct_name

def test_name_returns_default_root_name_when_po_is_a_root(mock_po_base):
    mock_po_base._name = None
    assert mock_po_base.name == PageObjectBase.DEFAULT_ROOT_NAME


def test_full_name_returns_correct_name_when_parent_exists(monkeypatch, mock_po_base):
    correct_name = 'child_full_name'
    class Parent:
        def _get_child_full_name(self, child): return correct_name
    monkeypatch.setattr(mock_po_base.__class__, 'parent', Parent())
    assert mock_po_base.full_name == correct_name

def test_full_name_returns_name_when_po_is_a_root(monkeypatch, mock_po_base):
    monkeypatch.setattr(mock_po_base.__class__, 'name', 'po_name')
    monkeypatch.setattr(mock_po_base.__class__, 'parent', None)
    assert mock_po_base.full_name == mock_po_base.name

