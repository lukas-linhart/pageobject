from pageobject import PageObject
from pageobject import PageObjectList
from pageobject import Select
from pageobject.pageobjectbase import PageObjectBase
import pytest


class MockPoTemplate(PageObject):
    def __init__(self): pass

@pytest.fixture
def mock_po():
    class MockPo(MockPoTemplate): pass
    return MockPo()

@pytest.fixture
def another_mock_po():
    class AnotherMockPo(MockPoTemplate): pass
    return AnotherMockPo()

@pytest.fixture
def yet_another_mock_po():
    class YetAnotherMockPo(MockPoTemplate): pass
    return YetAnotherMockPo()



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
        info = debug = lambda *args, **kwargs: None

    class MockWebElement(object):
        pass

    class MockCommandsPo(MockPoTemplate):
        @property
        def logger(self):
            return NopLogger()
        _log_id_short = None
        _log_id_long = None
        webelement = MockWebElement()

    return MockCommandsPo()

