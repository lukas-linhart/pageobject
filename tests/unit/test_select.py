import pytest
from .fixtures import mock_select
from selenium.webdriver.support.ui import Select as WebDriverSelect


def test_select_class_property_returns_a_webdriver_select_subclass(mock_select):
    assert issubclass(mock_select._select_class, WebDriverSelect)


def test_elem_property_returns_an_instance_of_webdriver_select(monkeypatch, mock_select):
    class MockWebDriverSelect(WebDriverSelect):
        def __init__(self, wd): pass
    monkeypatch.setattr(mock_select.__class__, '_select_class', MockWebDriverSelect)
    monkeypatch.setattr(mock_select.__class__, 'webelement', None)
    assert isinstance(mock_select.elem, WebDriverSelect)


def test_delegated_attributes_property_returns_a_set_of_strings(mock_select):
    assert isinstance(mock_select._delegated_attributes, set)
    assert all(isinstance(x, str) for x in mock_select._delegated_attributes)

