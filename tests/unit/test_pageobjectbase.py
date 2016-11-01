import pytest
import logging
from pageobject import PageObject
from pageobject.pageobjectbase import PageObjectBase
from .fixtures import mock_po_base
from selenium.webdriver import Remote as RemoteWebDriver


def test_dunder_repr_returns_correct_string(monkeypatch, mock_po_base):
    monkeypatch.setattr(mock_po_base.__class__, 'locator', '//body')
    assert repr(mock_po_base) == '<MockPoBase(MockPoBaseTemplate) (locator="{}")>'.format(
            mock_po_base.locator)


def test_default_locator_returns_None_when_not_provided():
    po = PageObjectBase()
    assert po.default_locator is None


def test_parent_locator_returns_correct_value_when_parent_is_valid(monkeypatch, mock_po_base):
    parent_locator = '//body'
    class Parent:
        locator = parent_locator
    mock_po_base.parent = Parent()
    assert mock_po_base._parent_locator == parent_locator

def test_parent_locator_returns_empty_string_when_parent_is_invalid(mock_po_base):
    mock_po_base.parent = None
    assert mock_po_base._parent_locator == ''

def test_locator_returns_default_locator_when_provided(monkeypatch, mock_po_base):
    locator = 'default'
    monkeypatch.setattr(mock_po_base.__class__, 'default_locator', locator)
    assert mock_po_base.locator == locator

def test_locator_returns_correct_value_when_chained(monkeypatch, mock_po_base):
    parent_locator = '//html'
    child_locator = '//body'
    mock_po_base._chain = True
    monkeypatch.setattr(mock_po_base.__class__, '_parent_locator', parent_locator)
    mock_po_base._locator = child_locator
    assert mock_po_base.locator == '{}{}'.format(parent_locator, child_locator)

def test_locator_returns_correct_value_when_not_chained(monkeypatch, mock_po_base):
    locator = '//body'
    mock_po_base._chain = False
    mock_po_base._locator = locator
    assert mock_po_base.locator == locator


def test_webdriver_returns_webdriver_of_a_parent_if_available(monkeypatch, mock_po_base):
    parent_webdriver = 'parent_webdriver'
    class Parent:
        webdriver = parent_webdriver
    mock_po_base.parent = Parent()
    assert mock_po_base.webdriver == parent_webdriver

def test_webdriver_returns_correct_value_if_valid(mock_po_base):
    class MockWebDriver(RemoteWebDriver):
        def __init__(self):  pass
        def __repr__(self): return 'MockWebDriver'
    mock_po_base.parent = None
    mock_po_base._webdriver = MockWebDriver()
    assert mock_po_base.webdriver == mock_po_base._webdriver

def test_webdriver_raises_AssertionException_when_invalid(mock_po_base):
    mock_po_base.parent = None
    mock_po_base._webdriver = None
    with pytest.raises(AssertionError):
        mock_po_base.webdriver


def test_logger_returns_parent_logger_if_available(mock_po_base):
    parent_logger = 'parent_logger'
    class Parent:
        logger = parent_logger
    mock_po_base.parent = Parent()
    assert mock_po_base.logger == parent_logger

def test_logger_returns_standard_logging_when_not_provided(mock_po_base):
    mock_po_base._logger = None
    assert mock_po_base.logger == logging

def test_logger_returns_initialized_value_if_valid(mock_po_base):
    mock_po_base.parent = None
    mock_po_base._logger = 'valid_logger'
    assert mock_po_base.logger == mock_po_base._logger

