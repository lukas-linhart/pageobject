import pytest
from pageobject import PageObject
from pageobject import PageObjectList
from selenium.webdriver import Remote as WebDriver


class MockWebDriver(WebDriver):
    def __init__(self): pass


def test_PO_registers_as_child_of_another_po_via_attribute_assignment():
    root_po = PageObject('')
    nested_po = PageObject('')
    root_po.nested_po = nested_po
    assert 'nested_po' in root_po.children
    assert nested_po.parent is root_po


def test_PO_registers_as_child_of_a_webdriver_via_attribute_assignment():
    wd = MockWebDriver()
    child_po = PageObject('')
    wd.child_po = child_po
    assert child_po.parent is wd


def test_POL_registers_as_child_of_a_po_via_attribute_assignment():
    root_po = PageObject('')
    nested_po_list = PageObjectList('')
    root_po.nested_po_list = nested_po_list
    assert 'nested_po_list' in root_po.children
    assert nested_po_list.parent is root_po


def test_POL_registers_as_child_of_a_webdriver_via_attribute_assignment():
    wd = MockWebDriver()
    child_po_list = PageObjectList('')
    wd.child_po_list = child_po_list
    assert child_po_list.parent is wd

