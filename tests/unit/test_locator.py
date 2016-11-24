import pytest
from pageobject.locator import Locator
from .fixtures import mock_locator


def test_constructor_inits_parameters_correctly():
    xpath = "//body"
    locator = Locator(xpath, 'dummy arg')
    assert locator._value == xpath


def test_value_property_return_correct_value(mock_locator):
    xpath = "//body"
    mock_locator._value = xpath
    assert mock_locator.value == xpath

