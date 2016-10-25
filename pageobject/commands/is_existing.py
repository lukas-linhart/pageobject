from selenium.common.exceptions import WebDriverException


def is_existing(self, log=True):
    if log:
        self.logger.info('determining whether {} is existing'.format(self._log_id_short))
        self.logger.debug('determining whether page object is existing; {}'.format(self._log_id_long))
    try:
        self.webelement
    except WebDriverException:
        if log:
            self.logger.info('{} is not existing'.format(self._log_id_short))
            self.logger.debug('page object is not existing; {}'.format(self._log_id_long))
        return False
    if log:
        self.logger.info('{} is existing'.format(self._log_id_short))
        self.logger.debug('page object is existing; {}'.format(self._log_id_long))
    return True

