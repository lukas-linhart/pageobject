def wait_for_vanish(self, timeout=None):
    """
    Wait fro page object to vanish from the DOM.

    :param int timeout: number of seconds to wait, if not provided
        :py:obj:`PageObject.DEFAULT_WAIT_TIMEOUT` is used
    """
    if timeout is None:
        timeout = self.DEFAULT_WAIT_TIMEOUT
    self.logger.info('waiting until page does not contain {}'.format(self._log_id_short))
    self.logger.debug('waiting until page does not contain page object; {}'.format(self._log_id_long))
    error_msg = 'Element "{}" still existing after {} seconds'.format(
        self._locator_value, timeout)
    self.wait_until(self.is_existing, func_kwargs=dict(log=False),
        timeout=timeout, error_msg=error_msg, reverse=True)
    self.logger.info('finished waiting until page does not contain {}'.format(self._log_id_short))
    self.logger.debug('finished waiting until page does not contain page object; {}'.format(self._log_id_long))
    return self

