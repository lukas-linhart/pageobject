import pytest
from pageobject import Page
from pageobject.locator import Locator


def test_constructor_inits_parameters_correctly():
    url = 'http://example.com'
    locator = '//body'
    chain = 'chain'
    webdriver = 'webdriver'
    logger = 'logger'
    name = 'name'
    page = Page(url=url, locator=locator, chain=chain, webdriver=webdriver,
            name=name)
    assert page._url == url
    assert isinstance(page._provided_locator, Locator)
    assert page._chain == chain
    assert page._webdriver == webdriver
    assert page._name == name

def test_constructor_calls_init_children_method():
    class MockPage(Page):
        def init_children(self):
            self.children_initialized = True
    page = MockPage()
    assert page.children_initialized is True

