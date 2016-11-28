def load(self, log=True):
    """
    Load the web page.

    :param bool log: whether to log or not (defualt is True)
    :returns: `self`
    :rtype: `PageObjectBase` instance
    """
    if log:
        self.logger.info('loading page (url "{}")'.format(self._url_value))
    self.webdriver.get(self._url_value)
    if log:
        self.logger.info('page loaded (url "{}")'.format(self._url_value))
    return self

