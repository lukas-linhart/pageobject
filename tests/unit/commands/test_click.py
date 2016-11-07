import pytest
from tests.unit.fixtures import mock_commands_po as mock_po


def test_click_method_returns_self(monkeypatch, mock_po):
    mock_po.webelement.click = lambda: None
    assert mock_po.click() == mock_po

