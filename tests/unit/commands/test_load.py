from pageobject import Page


def test_load_delegates_to_weebelement_and_returns_self():

    class MockWebDriver:
        def get(self, url): return None

    class MockPage(Page):
        def __init__(self): pass
        webdriver = MockWebDriver()
        _initialized_url = None

    mock_page = MockPage()
    assert mock_page.load() == mock_page

