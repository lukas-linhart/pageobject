def set_value(self, value):
    self.clear()
    self.logger.info('setting value of {} to "{}"'.format(self._log_id_short, value))
    self.logger.debug('setting value of page object to "{}"; {}'.format(value, self._log_id_long))
    self.webelement.send_keys(value)
    return self

