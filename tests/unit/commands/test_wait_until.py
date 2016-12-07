import pytest
from tests.unit.fixtures import mock_commands_po as mock_po
from selenium.common.exceptions import TimeoutException

def test_wait_until_raises_timeout_exception_when_deadline_is_reached(mock_po):
    with pytest.raises(TimeoutException):
        mock_po.wait_until(lambda: None)

def test_wait_until_returns_self_when_func_returns_true_and_reverse_is_false(mock_po):
    assert mock_po.wait_until(lambda: True) == mock_po

def test_wait_until_returns_self_when_func_returns_false_and_reverse_is_true(mock_po):
    assert mock_po.wait_until(lambda: False, reverse=True) == mock_po

