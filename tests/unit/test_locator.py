import pytest
from pageobject.locator import Locator
from pageobject.pageobjectbase import PageObjectBase
from .fixtures import mock_locator


def test_constructor_inits_parameters_correctly():
    xpath = "//body"
    locator = Locator(xpath, page_object=PageObjectBase())
    assert locator._initialized_value == xpath


def test_chain_property_returns_false_when_locator_starts_with_hashtag(mock_locator):
    mock_locator._initialized_value = "#spam"
    assert mock_locator.chain == False

def test_chain_property_returns_false_when_locator_starts_with_id(mock_locator):
    mock_locator._initialized_value = "id=spam"
    assert mock_locator.chain == False

def test_chain_property_returns_correct_value_when_locator_is_xpath(mock_locator):
    chain = 'chain'
    class MockPO:
        _chain = chain
    mock_locator._initialized_value = "//eggs"
    mock_locator._page_object = MockPO
    assert mock_locator.chain == MockPO._chain


def test_parent_locator_value_returns_correct_value_when_parent_exists(mock_locator):
    xpath = "//body"
    class MockPO:
        _parent_locator_value = xpath
    mock_locator._page_object = MockPO
    assert mock_locator.parent_locator_value == xpath


def test_xpath_returns_correct_value_for_locator_starting_with_hashtag(mock_locator):
    value = "#spam"
    mock_locator._initialized_value = value
    assert mock_locator._xpath == "//*[@id='spam']"

def test_xpath_returns_correct_value_for_locator_starting_with_id(mock_locator):
    value = "id=spam"
    mock_locator._initialized_value = value
    assert mock_locator._xpath == "//*[@id='spam']"

def test_xpath_returns_correct_value(mock_locator):
    value = "initialized"
    mock_locator._initialized_value = value
    assert mock_locator._xpath == value


def test_value_property_return_correct_nonchained_value(monkeypatch, mock_locator):
    xpath = "//body"
    monkeypatch.setattr(mock_locator.__class__, '_xpath', xpath)
    monkeypatch.setattr(mock_locator.__class__, 'chain', False)
    assert mock_locator.value == xpath


def test_value_property_returns_correct_chained_value(monkeypatch, mock_locator):
    parent_xpath = "//body"
    child_xpath = "//div"
    chained_xpath = '{}{}'.format(parent_xpath, child_xpath)

    monkeypatch.setattr(mock_locator.__class__, '_xpath', child_xpath)
    monkeypatch.setattr(mock_locator.__class__, 'chain', True)
    monkeypatch.setattr(mock_locator.__class__, 'parent_locator_value', parent_xpath)

    assert mock_locator.value == chained_xpath

