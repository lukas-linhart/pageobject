import pytest
from tests.unit.fixtures import mock_commands_po as mock_po


def test_get_attribute_method_delegates_to_webelement_and_returns_string(mock_po):
    attr = 'innerHTML'
    mock_po.webelement.get_attribute = lambda attribute, log=True: 'some text'
    assert isinstance(mock_po.get_attribute(attr), str)

