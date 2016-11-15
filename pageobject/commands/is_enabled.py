def is_enabled(self, log=True):
    if log:
        self.logger.info('determining whether {} is enabled'.format(self._log_id_short))
        self.logger.debug('determining whether page object is enabled; {}'.format(self._log_id_long))
    enabled = self.webelement.is_enabled()
    neg_str = '' if enabled else ' not'
    if log:
        self.logger.info('{} is{} enabled'.format(self._log_id_short, neg_str))
        self.logger.debug('page object is{} enabled; {}'.format(neg_str, self._log_id_long))
    return enabled

