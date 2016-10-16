from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from . import useless_logger


class PageObject(object):

    DEFAULT_NAME = 'page_object'
    DEFAULT_ROOT_NAME = 'root'

    def __init__(self, locator, parent, chain=True, webdriver=None, logger=useless_logger, name=None, children_class=None):
        self._locator = locator
        self.parent = parent
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._children_class = children_class

        self.init_children()


    def __repr__(self):
        my_class = self.__class__.__name__
        base_class = self.__class__.__bases__[0].__name__
        return '<{}({}) (locator="{}")>'.format(
                my_class, base_class, self.locator)


    def __getitem__(self, key):
        return self.children[key]


    def __len__(self):
        return len(self.children)


    def init_children(self):
        '''
        Meant to be overloaded by page objects
        containing other page objects.
        '''
        pass


    @property
    def locator(self):
        try:
            if self._chain:
                return self.parent.locator + self._locator
            else:
                return self._locator
        except AttributeError:
            return self._locator


    @property
    def webdriver(self):
        try:
            return self.parent.webdriver
        except AttributeError:
            return self._webdriver


    @property
    def logger(self):
        try:
            return self.parent.logger
        except AttributeError:
            return self._logger


    @property
    def children(self):
        return {attr_name: attr_value for attr_name, attr_value in self.__dict__.items()
                if isinstance(attr_value, PageObject)
                and attr_value is not self.parent}


    @property
    def name(self):
        if self._name:
            return self._name
        try:
            if isinstance(self.parent.children, list):
                return '{}[{}]'.format(self.parent.name, str(self.index))
            for child in self.parent.children:
                if self.parent.__dict__[child] == self:
                    return child
        except AttributeError:
            return PageObject.DEFAULT_ROOT_NAME
        except KeyError:
            return PageObject.DEFAULT_NAME


    @property
    def full_name(self):
        try:
            if isinstance(self.parent.children, dict):
                return '{}.{}'.format(self.parent.full_name, self.name)
            else:
                return '{}[{}]'.format(self.parent.full_name, str(self.index))
        except AttributeError:
            return self.name


    @property
    def children_class(self):
        raise NotImplementedError


    @property
    def _log_id_short(self):
        return 'page object "{}"'.format(self.name)


    @property
    def _log_id_long(self):
        return 'full name path: "{}", element: "{}"'.format(
                self.full_name, self.locator)


    def find(self, log=True):
        if log:
            self.logger.info('looking for {}'.format(self._log_id_short))
            self.logger.debug('looking for page object; {}'.format(self._log_id_long))
        elem = self.webdriver.find_element_by_xpath(self.locator)
        if log:
            self.logger.info('{} found'.format(self._log_id_short))
            self.logger.debug('page object found; {}'.format(self._log_id_long))
        return elem


    @property
    def text(self):
        return self.find(log=False).text


    def is_existing(self, log=True):
        if log:
            self.logger.info('determining whether {} is existing'.format(self._log_id_short))
            self.logger.debug('determining whether page object is existing; {}'.format(self._log_id_long))
        try:
            self.webdriver.find_element_by_xpath(self.locator)
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
        visible = self.find(log=log).is_displayed()
        neg_str = '' if visible else ' not'
        if log:
            self.logger.info('{} is{} visible'.format(self._log_id_short, neg_str))
            self.logger.debug('page object is{} visible; {}'.format(neg_str, self._log_id_long))
        return visible



    def wait_for_exist(self, timeout=60):
        self.logger.info('waiting until page contains {}'.format(self._log_id_short))
        self.logger.debug('waiting until page contains page object; {}'.format(self._log_id_long))
        WebDriverWait(self.webdriver, timeout).until(
                lambda x: self.is_existing(log=False),
                message='Element "{}" not found after {} seconds'.format(
                    self.locator, timeout))
        self.logger.info('finished waiting until page contains {}'.format(self._log_id_short))
        self.logger.debug('finished waiting until page contains page object; {}'.format(self._log_id_long))
        return self


    def wait_for_vanish(self, timeout=60):
        self.logger.info('waiting until page does not contain {}'.format(self._log_id_short))
        self.logger.debug('waiting until page does not contain page object; {}'.format(self._log_id_long))
        WebDriverWait(self.webdriver, timeout).until(
                lambda x: not self.is_existing(log=False),
                message='Element "{}" not found after {} seconds'.format(
                    self.locator, timeout))
        self.logger.info('finished waiting until page does not contain {}'.format(self._log_id_short))
        self.logger.debug('finished waiting until page does not contain page object; {}'.format(self._log_id_long))
        return self


    def wait_for_visible(self, timeout=60):
        self.logger.info('waiting until {} is visible'.format(self._log_id_short))
        self.logger.debug('waiting until page object is visible; {}'.format(self._log_id_long))
        WebDriverWait(self.webdriver, timeout).until(
                lambda x: self.is_visible(log=False),
                message='Element "{}" not visible after {} seconds'.format(
                    self.locator, timeout))
        self.logger.info('finished waiting until {} is visible'.format(self._log_id_short))
        self.logger.debug('finished waiting until page object is visible; {}'.format(self._log_id_long))
        return self


    def click(self):
        elem = self.find()
        self.logger.info('clicking on {}'.format(self._log_id_short))
        self.logger.debug('clicking on page object; {}'.format(self._log_id_long))
        elem.click()
        self.logger.info('successfully clicked on {}'.format(self._log_id_short))
        self.logger.debug('successfully clicked on page object; {}'.format(self._log_id_long))
        return self


    def clear(self, log=True, press_enter=False):
        elem = self.find(log=log)
        if log:
            self.logger.info('clearing {}'.format(self._log_id_short))
            self.logger.debug('clearing page object; {}'.format(self._log_id_long))
        elem.clear()
        if log:
            self.logger.info('{} cleared'.format(self._log_id_short))
            self.logger.debug('page object cleared; {}'.format(self._log_id_long))
        if press_enter:
            elem.send_keys(Keys.ENTER)
            if log:
                self.logger.info('"enter" key sent to {}'.format(self._log_id_short))
                self.logger.debug('"enter" key sent to page object; {}'.format(self._log_id_long))
        return self


    def get_value(self):
        elem = self.find()
        self.logger.info('getting value of {}'.format(self._log_id_short))
        self.logger.debug('getting value of page object; {}'.format(self._log_id_long))
        value = elem.get_attribute('value')
        self.logger.info('value of {} is "{}"'.format(self._log_id_short, value))
        self.logger.debug('value of page object is "{}"; {}'.format(value, self._log_id_long))
        return value


    def set_value(self, value):
        self.clear()
        elem = self.find(log=False)
        self.logger.info('setting value of {} to "{}"'.format(self._log_id_short, value))
        self.logger.debug('setting value of page object to "{}"; {}'.format(value, self._log_id_long))
        elem.send_keys(value)
        return self


    def get_attribute(self, attribute, log=True):
        if log:
            self.logger.info('getting attribute "{}" of {}'.format(attribute, self._log_id_short))
            self.logger.debug('getting attribute "{}" of page object; {}'.format(attribute, self._log_id_long))
        return self.find(log=log).get_attribute(attribute)


    def move_to(self):
        self.logger.info('moving to {}'.format(self._log_id_short))
        self.logger.debug('moving to page object; {}'.format(self._log_id_long))
        action = ActionChains(self.webdriver).move_to_element(self.find())
        action.perform()
        return self


    def send_keys(self, keys, log=True):
        elem = self.find(log=log)
        single_keys = keys_to_typing(keys)
        if log:
            self.logger.info('sending keys {} to {}'.format(single_keys, self._log_id_short))
            self.logger.debug('sending keys {} to page object; {}'.format(single_keys, self._log_id_long))
        elem.send_keys(keys)
        return self

