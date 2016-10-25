from selenium.webdriver.common.utils import keys_to_typing


def send_keys(self, keys, log=True):
    single_keys = keys_to_typing(keys)
    if log:
        self.logger.info('sending keys {} to {}'.format(single_keys, self._log_id_short))
        self.logger.debug('sending keys {} to page object; {}'.format(single_keys, self._log_id_long))
    self.webelement.send_keys(keys)
    return self

