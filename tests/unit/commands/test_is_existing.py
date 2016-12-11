from tests.unit.fixtures import mock_commands_po as mock_po
from selenium.common.exceptions import WebDriverException


def test_is_existing_method_returns_True_if_no_exception(mock_po):
    assert mock_po.is_existing() == True

def test_is_existing_method_returns_False_if_exception(monkeypatch, mock_po):
    @property
    def failing_webelement(self):
        raise WebDriverException
    monkeypatch.setattr(mock_po.__class__, 'webelement', failing_webelement)
    assert mock_po.is_existing() == False

