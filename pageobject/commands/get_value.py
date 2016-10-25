def get_value(self):
    self.logger.info('getting value of {}'.format(self._log_id_short))
    self.logger.debug('getting value of page object; {}'.format(self._log_id_long))
    value = self.webelement.get_attribute('value')
    self.logger.info('value of {} is "{}"'.format(self._log_id_short, value))
    self.logger.debug('value of page object is "{}"; {}'.format(value, self._log_id_long))
    return value

