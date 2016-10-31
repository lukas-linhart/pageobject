from pageobject import PageObject
import pytest


@pytest.fixture
def mock_po():
    class MockPo(PageObject):
        def __init__(self): pass
    return MockPo()

@pytest.fixture
def another_mock_po():
    class AnotherMockPo(PageObject):
        def __init__(self): pass
    return AnotherMockPo()

@pytest.fixture
def yet_another_mock_po():
    class YetAnotherMockPo(PageObject):
        def __init__(self): pass
    return YetAnotherMockPo()

