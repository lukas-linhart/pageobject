import pytest
from .fixtures import mock_select
from selenium.webdriver.support.ui import Select as WebDriverSelect


def test_elem_property_returns_an_instance_of_webdriver_select(monkeypatch, mock_select):
    class MockWebDriverSelect(WebDriverSelect):
        def __init__(self, wd): pass
    monkeypatch.setattr(mock_select.__class__, '_select_class', MockWebDriverSelect)
    monkeypatch.setattr(mock_select.__class__, 'webelement', None)
    assert isinstance(mock_select.elem, WebDriverSelect)
