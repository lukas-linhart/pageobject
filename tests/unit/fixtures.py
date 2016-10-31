from pageobject import PageObject
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

