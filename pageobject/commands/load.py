def load(self, log=True):
    if log:
        self.logger.info('loading page (url "{}")'.format(self._url))
    self.webdriver.get(self._url)
    if log:
        self.logger.info('page loaded (url "{}")'.format(self._url))
    return self

