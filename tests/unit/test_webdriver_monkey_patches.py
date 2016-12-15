import pytest
from selenium.webdriver import Remote as WebDriver
from pageobject.pageobjectbase import PageObjectBase


class MockWebDriver(WebDriver):
    def __init__(self): pass


class MockPo(PageObjectBase):
    def __init__(self): pass


def test_setattr_specia_method_sets_non_po_attributes_correctly():
    wd = MockWebDriver()
    child = 'spam'
    wd.child = child
    assert wd.child == child
    with pytest.raises(AttributeError):
        wd.child._parent


def test_setattr_special_method_sets_po_attributes_correctly():
    wd = MockWebDriver()
    child = MockPo()
    wd.child = child
    assert wd.child == child
    assert wd.child._parent == wd

