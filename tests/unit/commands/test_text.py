import pytest
from tests.unit.fixtures import mock_commands_po as mock_po


def test_text_property_delegates_to_webelement_and_returns_string(mock_po):
    text = 'html'
    mock_po.webelement.text = text
    assert isinstance(mock_po.text, str)

