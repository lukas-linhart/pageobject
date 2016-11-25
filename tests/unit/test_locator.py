import pytest
from pageobject.locator import Locator
from pageobject.pageobjectbase import PageObjectBase
from .fixtures import mock_locator


def test_constructor_inits_parameters_correctly():
    xpath = "//body"
    locator = Locator(xpath, 'dummy arg', page_object=PageObjectBase())
    assert locator._value == xpath


def test_constructor_raises_AssertionError_when_po_is_not_a_po():
    xpath = "//body"
    with pytest.raises(AssertionError):
        locator = Locator(xpath, page_object=None)


def test_chain_property_returns_correct_value(mock_locator):
    chain = 'chain'
    class MockPO:
        _chain = chain
    mock_locator.page_object = MockPO
    assert mock_locator.chain == MockPO._chain


def test_parent_locator_value_returns_correct_value_when_parent_exists(monkeypatch, mock_locator):
    xpath = "//body"

    class MockPO:
        _parent_locator = lambda: None
        _parent_locator.value = xpath
    mock_locator.page_object = MockPO

    assert mock_locator.parent_locator_value == xpath


def test_value_property_return_correct_nonchained_value(monkeypatch, mock_locator):
    xpath = "//body"
    mock_locator._value = xpath
    monkeypatch.setattr(mock_locator.__class__, 'chain', False)
    assert mock_locator.value == xpath


def test_value_property_returns_correct_chained_value(monkeypatch, mock_locator):
    parent_xpath = "//body"
    child_xpath = "//div"
    chained_xpath = '{}{}'.format(parent_xpath, child_xpath)

    mock_locator._value = child_xpath
    monkeypatch.setattr(mock_locator.__class__, 'chain', True)
    monkeypatch.setattr(mock_locator.__class__, 'parent_locator_value', parent_xpath)

    assert mock_locator.value == chained_xpath

