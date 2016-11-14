from selenium.webdriver.common.keys import Keys


def set_value(self, value, press_enter=False):
    self.clear()
    self.logger.info('setting value of {} to "{}"'.format(self._log_id_short, value))
    self.logger.debug('setting value of page object to "{}"; {}'.format(value, self._log_id_long))
    self.webelement.send_keys(value)
    if press_enter:
        self.webelement.send_keys(Keys.ENTER)
    return self

