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

def test_wait_until_accepts_func_args(mock_po):
    fargs = list('spam')
    def f(s, p, a, m):
        if [s, p, a, m] == fargs:
            return True
    mock_po.wait_until(f, func_args=fargs)

def test_wait_until_accepts_func_kwargs(mock_po):
    fkwargs = dict(a=1, b=2)
    def f(a=None, b=None):
        if [a, b] == [1, 2]:
            return True
    mock_po.wait_until(f, func_kwargs=fkwargs)

