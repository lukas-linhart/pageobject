from pageobject.pageobjectbase import PageObjectBase


def wait_for_visible(self, timeout=None):
    if timeout is None:
        timeout = PageObjectBase.DEFAULT_WAIT_TIMEOUT
    self.logger.info('waiting until {} is visible'.format(self._log_id_short))
    self.logger.debug('waiting until page object is visible; {}'.format(self._log_id_long))
    error_msg = 'Element "{}" still not visible after {} seconds'.format(
        self.locator, timeout)
    self.wait_until(self.is_visible, func_kwargs=dict(log=False),
        timeout=timeout, error_msg=error_msg)
    self.logger.info('finished waiting until {} is visible'.format(self._log_id_short))
    self.logger.debug('finished waiting until page object is visible; {}'.format(self._log_id_long))
    return self

