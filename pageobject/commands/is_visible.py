def is_visible(self, log=True):
    """
    Return True if page object is visible, False otherwise.

    :param bool log: whether to log or not (default is True)
    :returns: whether page object is visible
    :rtype: bool
    """
    if log:
        self.logger.info('determining whether page object {} is visible'.format(self._log_id_short))
    self.logger.debug('determining whether page object is visible; {}'.format(self._log_id_long))
    visible = self.webelement.is_displayed()
    neg_str = '' if visible else ' not'
    if log:
        self.logger.info('page object {} is{} visible'.format(self._log_id_short, neg_str))
    self.logger.debug('page object is{} visible; {}'.format(neg_str, self._log_id_long))
    return visible

