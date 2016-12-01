def wait_for_interactive(self, timeout=None):
    """
    Wait for page object to be interactive.

    :param int timeout: number of seconds to wait, if not provided
        PageObject.DEFAULT_WAIT_TIMEOUT is used
    """
    if timeout is None:
        timeout = self.__class__.DEFAULT_WAIT_TIMEOUT
    self.logger.info('waiting until page object is interactive; {}'.format(
        self._log_id_long))
    error_msg = ('page object still not interactive after {} seconds;'
        + ' {}').format(timeout, self._log_id_long)
    self.wait_until(self.is_interactive, func_kwargs=dict(log=False),
        timeout=timeout, error_msg=error_msg)
    self.logger.info(('finished waiting until page object is interactive;'
        + ' {}').format(self._log_id_long))
    return self

