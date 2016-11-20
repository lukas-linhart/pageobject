def load(self, log=True):
    """
    Load the web page.

    :param bool log: whether to log or not (defualt is True)
    :returns: `self`
    :rtype: `PageObjectBase` instance
    """
    if log:
        self.logger.info('loading page (url "{}")'.format(self._url))
    self.webdriver.get(self._url)
    if log:
        self.logger.info('page loaded (url "{}")'.format(self._url))
    return self

