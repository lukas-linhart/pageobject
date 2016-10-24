import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, TimeoutException

from .pageobjectbase import PageObjectBase


class PageObject(PageObjectBase):

    DEFAULT_WAIT_TIMEOUT = 60
    DEFAULT_POLL_INTERVAL = 0.25


    def __init__(self, locator, parent, chain=True, webdriver=None, logger=None, name=None):
        self._locator = locator
        self.parent = parent
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name

        try:
            self.parent.register_child(self)
        except AttributeError:
            pass

        self.init_children()


    def __bool__(self):
        return self.is_existing(log=False)


    def __getitem__(self, key):
        return self.children[key]


    def __len__(self):
        return len(self.children)


    def register_child(self, child):
        try:
            self.__setattr__(child.name, child)
        except TypeError:
            return


    def init_children(self):
        """
        Meant to be overloaded by page objects
        containing other page objects.
        """
        pass


    @property
    def children(self):
        return {attr_name: attr_value for attr_name, attr_value in self.__dict__.items()
                if isinstance(attr_value, PageObjectBase)
                and attr_value is not self.parent}


    @property
    def webelement(self):
        return self.webdriver.find_element_by_xpath(self.locator)


    @property
    def text(self):
        return self.webelement.text


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


    def is_visible(self, log=True):
        if log:
            self.logger.info('determining whether {} is visible'.format(self._log_id_short))
            self.logger.debug('determining whether page object is visible; {}'.format(self._log_id_long))
        visible = self.webelement.is_displayed()
        neg_str = '' if visible else ' not'
        if log:
            self.logger.info('{} is{} visible'.format(self._log_id_short, neg_str))
            self.logger.debug('page object is{} visible; {}'.format(neg_str, self._log_id_long))
        return visible


    def wait_until(self, func, func_args=[], func_kwargs={},
            timeout=DEFAULT_WAIT_TIMEOUT, error_msg=None, reverse=False):
        deadline = time.time() + timeout
        while time.time() < deadline:
            if func(*func_args, **func_kwargs) is not reverse:
                return self
            time.sleep(PageObject.DEFAULT_POLL_INTERVAL)
        if error_msg is None:
            error_msg = ('function {} called with args {} and kwargs '
                        + '{} still returns {} after {} seconds').format(
                    func, func_args, func_kwargs, reverse, timeout)
        raise TimeoutException(error_msg)


    def wait_for_exist(self, timeout=DEFAULT_WAIT_TIMEOUT):
        self.logger.info('waiting until page contains {}'.format(self._log_id_short))
        self.logger.debug('waiting until page contains page object; {}'.format(self._log_id_long))
        error_msg = 'Element "{}" still not existing after {} seconds'.format(
            self.locator, timeout)
        self.wait_until(self.is_existing, func_kwargs=dict(log=False),
            timeout=timeout, error_msg=error_msg)
        self.logger.info('finished waiting until page contains {}'.format(self._log_id_short))
        self.logger.debug('finished waiting until page contains page object; {}'.format(self._log_id_long))
        return self


    def wait_for_vanish(self, timeout=DEFAULT_WAIT_TIMEOUT):
        self.logger.info('waiting until page does not contain {}'.format(self._log_id_short))
        self.logger.debug('waiting until page does not contain page object; {}'.format(self._log_id_long))
        error_msg = 'Element "{}" still existing after {} seconds'.format(
            self.locator, timeout)
        self.wait_until(self.is_existing, func_kwargs=dict(log=False),
            timeout=timeout, error_msg=error_msg, reverse=True)
        self.logger.info('finished waiting until page does not contain {}'.format(self._log_id_short))
        self.logger.debug('finished waiting until page does not contain page object; {}'.format(self._log_id_long))
        return self


    def wait_for_visible(self, timeout=DEFAULT_WAIT_TIMEOUT):
        self.logger.info('waiting until {} is visible'.format(self._log_id_short))
        self.logger.debug('waiting until page object is visible; {}'.format(self._log_id_long))
        error_msg = 'Element "{}" still not visible after {} seconds'.format(
            self.locator, timeout)
        self.wait_until(self.is_visible, func_kwargs=dict(log=False),
            timeout=timeout, error_msg=error_msg)
        self.logger.info('finished waiting until {} is visible'.format(self._log_id_short))
        self.logger.debug('finished waiting until page object is visible; {}'.format(self._log_id_long))
        return self


    def click(self):
        self.logger.info('clicking on {}'.format(self._log_id_short))
        self.logger.debug('clicking on page object; {}'.format(self._log_id_long))
        self.webelement.click()
        self.logger.info('successfully clicked on {}'.format(self._log_id_short))
        self.logger.debug('successfully clicked on page object; {}'.format(self._log_id_long))
        return self


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


    def get_value(self):
        self.logger.info('getting value of {}'.format(self._log_id_short))
        self.logger.debug('getting value of page object; {}'.format(self._log_id_long))
        value = self.webelement.get_attribute('value')
        self.logger.info('value of {} is "{}"'.format(self._log_id_short, value))
        self.logger.debug('value of page object is "{}"; {}'.format(value, self._log_id_long))
        return value


    def set_value(self, value):
        self.clear()
        self.logger.info('setting value of {} to "{}"'.format(self._log_id_short, value))
        self.logger.debug('setting value of page object to "{}"; {}'.format(value, self._log_id_long))
        self.webelement.send_keys(value)
        return self


    def get_attribute(self, attribute, log=True):
        if log:
            self.logger.info('getting attribute "{}" of {}'.format(attribute, self._log_id_short))
            self.logger.debug('getting attribute "{}" of page object; {}'.format(attribute, self._log_id_long))
        return self.webelement.get_attribute(attribute)


    def move_to(self):
        self.logger.info('moving to {}'.format(self._log_id_short))
        self.logger.debug('moving to page object; {}'.format(self._log_id_long))
        action = ActionChains(self.webdriver).move_to_element(self.webelement)
        action.perform()
        return self


    def send_keys(self, keys, log=True):
        single_keys = keys_to_typing(keys)
        if log:
            self.logger.info('sending keys {} to {}'.format(single_keys, self._log_id_short))
            self.logger.debug('sending keys {} to page object; {}'.format(single_keys, self._log_id_long))
        self.webelement.send_keys(keys)
        return self

