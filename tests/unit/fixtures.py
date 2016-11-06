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

