import time
from selenium.common.exceptions import TimeoutException
from pageobject.pageobjectbase import PageObjectBase


def wait_until(self, func, func_args=[], func_kwargs={},
        timeout=None, error_msg=None, reverse=False):
    if timeout is None:
        timeout = PageObjectBase.DEFAULT_WAIT_TIMEOUT
    deadline = time.time() + timeout
    while time.time() < deadline:
        if func(*func_args, **func_kwargs) is not reverse:
            return self
        time.sleep(PageObjectBase.DEFAULT_POLL_INTERVAL)
    if error_msg is None:
        error_msg = ('function {} called with args {} and kwargs '
                    + '{} still returns {} after {} seconds').format(
                func, func_args, func_kwargs, reverse, timeout)
    raise TimeoutException(error_msg)

