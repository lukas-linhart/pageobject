import time
from selenium.common.exceptions import TimeoutException


DEFAULT_WAIT_TIMEOUT = 60
DEFAULT_POLL_INTERVAL = 0.25


def wait_until(self, func, func_args=[], func_kwargs={},
        timeout=DEFAULT_WAIT_TIMEOUT, error_msg=None, reverse=False):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if func(*func_args, **func_kwargs) is not reverse:
            return self
        time.sleep(DEFAULT_POLL_INTERVAL)
    if error_msg is None:
        error_msg = ('function {} called with args {} and kwargs '
                    + '{} still returns {} after {} seconds').format(
                func, func_args, func_kwargs, reverse, timeout)
    raise TimeoutException(error_msg)

