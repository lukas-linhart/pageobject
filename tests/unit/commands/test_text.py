import pytest
from tests.unit.fixtures import mock_commands_po as mock_po


def test_text_delegates_to_webelement(mock_po):
    text = 'html'
    mock_po.webelement.text = text
    assert mock_po.text == text

