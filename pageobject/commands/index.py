from selenium.common.exceptions import StaleElementReferenceException


def index(self, value, attempt=1):
    if attempt == 1:
        self.logger.info('getting index of "{}" within {}'.format(value, self._log_id_short))
    self.logger.debug('getting index of "{}" within page object, attempt number {}; {}'.format(value, attempt, self._log_id_long))
    try:
        index = [item.text for item in self[:]].index(value)
        self.logger.info('index of "{}" within {} is {}'.format(value, self._log_id_short, index))
        self.logger.debug('index of "{}" within page object is {}; {}'.format(value, index, self._log_id_long))
        return index
    except StaleElementReferenceException:
        self.logger.debug('getting index failed, trying again')
        return self.index(value, attempt=attempt+1)

