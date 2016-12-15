from pageobject import PageObject
from pageobject import PageObjectList
from selenium.webdriver import Remote as WebDriver


class MockWebDriver(WebDriver):
    def __init__(self): pass


def test_root_PO_has_correct_short_implicit_name_when_not_a_child_of_webdriver():
    root_po = PageObject(None)
    assert root_po.name == root_po.__class__.DEFAULT_ROOT_NAME


def test_root_PO_has_correct_short_implicit_name_when_being_a_child_of_webdriver():
    wd = MockWebDriver()
    root_po = PageObject(None)
    wd.root_po = root_po
    assert root_po.name == root_po.__class__.DEFAULT_ROOT_NAME


def test_root_PO_has_correct_short_explicit_name():
    po_name = 'explicit_name'
    root_po = PageObject(None, name=po_name)
    assert root_po.name == po_name


def test_root_PO_has_equal_short_and_full_names():
    wd = MockWebDriver()
    root_po = PageObject(None)
    wd.root_po = root_po
    assert root_po.name == root_po.full_name


def test_nested_PO_has_correct_short_name_when_explicit_name_not_provided():
    root_po = PageObject(None)
    root_po.nested_po = PageObject(None)
    assert root_po.nested_po.name == 'nested_po'


def test_nested_PO_explicit_name_is_ignored():
    root_po = PageObject(None)
    root_po.nested_po = PageObject(None, name='explicit_name')
    assert root_po.nested_po.name == 'nested_po'


def test_nested_PO_has_correct_full_name():
    wd = MockWebDriver()
    root_po, nested_po, leaf_po = (PageObject(None) for x in range(3))
    wd.root_po = root_po
    root_po.nested_po = nested_po
    nested_po.leaf_po = leaf_po
    separator = PageObject.NAME_SEPARATOR
    leaf_po_full_name = '{}{}{}{}{}'.format(
            root_po.name, separator, nested_po.name,
            separator, leaf_po.name)
    assert leaf_po.full_name == leaf_po_full_name

