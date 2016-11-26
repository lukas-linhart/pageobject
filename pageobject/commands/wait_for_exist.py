def wait_for_exist(self, timeout=None):
    """
    Wait for page object to exist in the DOM.

    :param int timeout: number of seconds to wait, if not provided
        :py:obj:`PageObject.DEFAULT_WAIT_TIMEOUT` is used
    """
    if timeout is None:
        timeout = self.__class__.DEFAULT_WAIT_TIMEOUT
    self.logger.info('waiting until page contains {}'.format(self._log_id_short))
    self.logger.debug('waiting until page contains page object; {}'.format(self._log_id_long))
    error_msg = 'Element "{}" still not existing after {} seconds'.format(
        self._locator_value, timeout)
    self.wait_until(self.is_existing, func_kwargs=dict(log=False),
        timeout=timeout, error_msg=error_msg)
    self.logger.info('finished waiting until page contains {}'.format(self._log_id_short))
    self.logger.debug('finished waiting until page contains page object; {}'.format(self._log_id_long))
    return self

