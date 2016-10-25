def get_attribute(self, attribute, log=True):
    if log:
        self.logger.info('getting attribute "{}" of {}'.format(attribute, self._log_id_short))
        self.logger.debug('getting attribute "{}" of page object; {}'.format(attribute, self._log_id_long))
    return self.webelement.get_attribute(attribute)

