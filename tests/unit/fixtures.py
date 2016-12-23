from pageobject import PageObject
from pageobject import Page
from pageobject import PageObjectList
from pageobject import Select
from pageobject.pageobjectbase import PageObjectBase
from pageobject.locator import Locator
import pytest


# TODO - delete once all unit tests use their own fixtures
class MockPoTemplate(PageObject):
    def __init__(self): pass

@pytest.fixture
def mock_po():
    class MockPo(MockPoTemplate): pass
    return MockPo()


class MockPageTemplate(Page):
    def __init__(self): pass

@pytest.fixture
def mock_page():
    class MockPage(MockPageTemplate): pass
    return MockPage()


class MockPoBaseTemplate(PageObjectBase):
    def __init__(self): pass

@pytest.fixture
def mock_po_base():
    class MockPoBase(MockPoBaseTemplate): pass
    return MockPoBase()


class MockPoListTemplate(PageObjectList):
    def __init__(self): pass

@pytest.fixture
def mock_po_list():
    class MockPoList(MockPoListTemplate): pass
    return MockPoList()


class MockSelectTemplate(Select):
    def __init__(self): pass

@pytest.fixture
def mock_select():
    class MockSelect(MockSelectTemplate): pass
    return MockSelect()


@pytest.fixture
def mock_commands_po():

    class NopLogger(object):
        info = debug = warning = lambda *args, **kwargs: None

    class MockWebElement(object):
        pass

    class MockCommandsPo(MockPoTemplate):
        @property
        def logger(self):
            return NopLogger()
        _log_id_short = None
        _log_id_long = None
        DEFAULT_WAIT_TIMEOUT = 0.0001
        DEFAULT_POLL_INTERVAL = 0.000001
        webelement = MockWebElement()

    return MockCommandsPo()


class MockLocatorTemplate(Locator):
    def __init__(self): pass

@pytest.fixture
def mock_locator():

    class MockLocator(MockLocatorTemplate): pass
    return MockLocator()

