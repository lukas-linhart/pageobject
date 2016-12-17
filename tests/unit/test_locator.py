import pytest
from pageobject.locator import Locator
from pageobject.pageobjectbase import PageObjectBase
from .fixtures import mock_locator


def test_constructor_inits_parameters_correctly():
    xpath = "//body"
    locator = Locator(xpath, page_object=PageObjectBase())
    assert locator._initialized_value == xpath


def test_initialized_type_returns_empty_when_val_is_empty_string(mock_locator):
    mock_locator._initialized_value = ''
    assert mock_locator._initialized_type == 'empty'

def test_initialized_type_returns_id_when_val_starts_with_hashtag(mock_locator):
    mock_locator._initialized_value = '#some_id'
    assert mock_locator._initialized_type == 'id'

def test_initialized_type_returns_id_when_val_starts_with_id(mock_locator):
    mock_locator._initialized_value = 'id=some_id'
    assert mock_locator._initialized_type == 'id'

def test_initialized_type_returns_xpath_when_val_starts_with_left_paren(mock_locator):
    mock_locator._initialized_value = '(//div)[3]'
    assert mock_locator._initialized_type == 'xpath'

def test_initialized_type_returns_xpath_when_val_starts_with_slash(mock_locator):
    mock_locator._initialized_value = '/div'
    assert mock_locator._initialized_type == 'xpath'

def test_initialized_type_returns_xpath_when_val_starts_with_dot_slash(mock_locator):
    mock_locator._initialized_value = './div'
    assert mock_locator._initialized_type == 'xpath'

def test_initialized_type_returns_xpath_when_val_starts_with_doubledot_slash(mock_locator):
    mock_locator._initialized_value = '../div'
    assert mock_locator._initialized_type == 'xpath'

def test_initialized_type_returns_xpath_when_val_starts_with_asterisk_slash(mock_locator):
    mock_locator._initialized_value = '*/div'
    assert mock_locator._initialized_type == 'xpath'

def test_initialized_type_returns_attribute_when_val_starts_with_at_char(mock_locator):
    mock_locator._initialized_value = '@test-id'
    assert mock_locator._initialized_type == 'attribute'

def test_initialized_type_raises_ValueError_by_default(mock_locator):
    mock_locator._initialized_value = 'some_locator'
    with pytest.raises(ValueError):
        mock_locator._initialized_type


def test_chain_property_returns_false_when_parent_locator_value_is_none(monkeypatch, mock_locator):
    monkeypatch.setattr(mock_locator.__class__, '_parent_locator_value', None)
    assert mock_locator._chain == False

def test_chain_property_returns_false_when_initialized_type_is_id(monkeypatch, mock_locator):
    monkeypatch.setattr(mock_locator.__class__, '_parent_locator_value', 'not_none')
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'id')
    assert mock_locator._chain == False

def test_chain_property_returns_correct_value_when_initialized_type_is_not_id(monkeypatch, mock_locator):
    monkeypatch.setattr(mock_locator.__class__, '_parent_locator_value', 'not_none')
    class MockPO:
        _chain = 'chain'
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'not_an_id')
    mock_locator._page_object = MockPO
    assert mock_locator._chain == MockPO._chain


def test_parent_locator_value_returns_correct_value_when_parent_exists(mock_locator):
    xpath = "//body"
    class MockPO:
        _parent_locator_value = xpath
    mock_locator._page_object = MockPO
    assert mock_locator._parent_locator_value == xpath


def test_id_to_xpath_returns_correct_value_for_id_starting_with_hashtag(mock_locator):
    assert mock_locator._id_to_xpath('#spam') == "//*[@id='spam']"

def test_id_to_xpath_returns_correct_value_for_id_starting_with_id(mock_locator):
    assert mock_locator._id_to_xpath('id=spam') == "//*[@id='spam']"


def test_attribute_to_xpath_returns_correct_value(mock_locator):
    assert mock_locator._attribute_to_xpath('@test-id=login_form') == "//*[@test-id='login_form']"


def test_xpath_calls_id_to_xpath_with_correct_parameter(monkeypatch, mock_locator):
    spam = 'spam'
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'id')
    mock_locator._initialized_value = spam
    mock_locator._id_to_xpath = lambda value: spam
    assert mock_locator._xpath == spam

def test_xpath_calls_attribute_to_xpath_with_correct_parameter(monkeypatch, mock_locator):
    spam = 'spam'
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'attribute')
    mock_locator._initialized_value = spam
    mock_locator._attribute_to_xpath = lambda value: spam
    assert mock_locator._xpath == spam

def test_xpath_returns_correct_value_for_xpath_locator(monkeypatch, mock_locator):
    value = "initialized"
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'xpath')
    mock_locator._initialized_value = value
    assert mock_locator._xpath == value

def test_xpath_returns_correct_value_for_empty_locator(monkeypatch, mock_locator):
    value = ""
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'empty')
    mock_locator._initialized_value = value
    assert mock_locator._xpath == value

def test_xpath_raises_ValueError_for_unsupported_types(monkeypatch, mock_locator):
    monkeypatch.setattr(mock_locator.__class__, '_initialized_type', 'unsupported')
    with pytest.raises(ValueError):
        mock_locator._xpath


def test_value_property_return_correct_nonchained_value(monkeypatch, mock_locator):
    xpath = "//body"
    monkeypatch.setattr(mock_locator.__class__, '_xpath', xpath)
    monkeypatch.setattr(mock_locator.__class__, '_chain', False)
    assert mock_locator.value == xpath


def test_value_property_returns_correct_chained_value(monkeypatch, mock_locator):
    parent_xpath = "//body"
    child_xpath = "//div"
    chained_xpath = '{}{}'.format(parent_xpath, child_xpath)

    monkeypatch.setattr(mock_locator.__class__, '_xpath', child_xpath)
    monkeypatch.setattr(mock_locator.__class__, '_chain', True)
    monkeypatch.setattr(mock_locator.__class__, '_parent_locator_value', parent_xpath)

    assert mock_locator.value == chained_xpath

