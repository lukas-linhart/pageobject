import pytest
from tests.unit.fixtures import mock_po


def test_webelement_calls_correct_wd_method_with_correct_parameter(monkeypatch, mock_po):
    class MockWebDriver:
        def find_element_by_xpath(self, xpath):
           self.xpath = xpath
    locator_value = "//body"
    monkeypatch.setattr(mock_po.__class__, '_locator_value', locator_value)
    monkeypatch.setattr(mock_po.__class__, 'webdriver', MockWebDriver())
    mock_po.webelement
    assert mock_po.webdriver.xpath == mock_po._locator_value

