import pytest
from tests.unit.fixtures import mock_commands_po as mock_po


def test_get_value_method_delegates_to_webelement_with_correct_parameter(mock_po):
    correct_parameter = 'value'
    mock_po.webelement.get_attribute = lambda attr, log=True: attr
    assert mock_po.get_value() == correct_parameter

