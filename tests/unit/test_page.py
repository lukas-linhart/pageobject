import pytest
from pageobject import Page
from pageobject.locator import Locator
from .fixtures import mock_page


def test_constructor_inits_parameters_correctly():
    url = 'http://example.com'
    locator = '//body'
    chain = 'chain'
    webdriver = 'webdriver'
    logger = 'logger'
    name = 'name'
    page = Page(url=url, locator=locator, chain=chain, webdriver=webdriver,
            name=name)
    assert page._initialized_url == url
    assert page._initialized_locator == locator
    assert page._chain == chain
    assert page._webdriver == webdriver
    assert page._name == name

def test_constructor_calls_init_children_method():
    class MockPage(Page):
        def init_children(self):
            self.children_initialized = True
    page = MockPage()
    assert page.children_initialized is True


def test_provided_url_returns_requested_url_when_provided(monkeypatch, mock_page):
    requested_url = "requested"
    monkeypatch.setattr(mock_page.__class__, 'requested_url', requested_url)
    assert mock_page._provided_url == requested_url

def test_provided_url_returns_initialized_url_when_requested_url_not_provided(monkeypatch, mock_page):
    initialized_url = "initialized"
    mock_page._initialized_url = initialized_url
    assert mock_page._provided_url == initialized_url

