DEFAULT_WAIT_TIMEOUT = 60


def wait_for_exist(self, timeout=DEFAULT_WAIT_TIMEOUT):
    self.logger.info('waiting until page contains {}'.format(self._log_id_short))
    self.logger.debug('waiting until page contains page object; {}'.format(self._log_id_long))
    error_msg = 'Element "{}" still not existing after {} seconds'.format(
        self.locator, timeout)
    self.wait_until(self.is_existing, func_kwargs=dict(log=False),
        timeout=timeout, error_msg=error_msg)
    self.logger.info('finished waiting until page contains {}'.format(self._log_id_short))
    self.logger.debug('finished waiting until page contains page object; {}'.format(self._log_id_long))
    return self

