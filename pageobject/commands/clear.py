from selenium.webdriver.common.keys import Keys


def clear(self, log=True, press_enter=False):
    if log:
        self.logger.info('clearing {}'.format(self._log_id_short))
        self.logger.debug('clearing page object; {}'.format(self._log_id_long))
    self.webelement.clear()
    if log:
        self.logger.info('{} cleared'.format(self._log_id_short))
        self.logger.debug('page object cleared; {}'.format(self._log_id_long))
    if press_enter:
        self.webelement.send_keys(Keys.ENTER)
        if log:
            self.logger.info('"enter" key sent to {}'.format(self._log_id_short))
            self.logger.debug('"enter" key sent to page object; {}'.format(self._log_id_long))
    return self

