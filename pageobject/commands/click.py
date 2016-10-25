def click(self):
    self.logger.info('clicking on {}'.format(self._log_id_short))
    self.logger.debug('clicking on page object; {}'.format(self._log_id_long))
    self.webelement.click()
    self.logger.info('successfully clicked on {}'.format(self._log_id_short))
    self.logger.debug('successfully clicked on page object; {}'.format(self._log_id_long))
    return self

