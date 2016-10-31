import logging
from selenium.webdriver import Remote as WebDriver


class PageObjectBase(object):

    DEFAULT_NAME = 'page_object'
    DEFAULT_ROOT_NAME = 'root'
    NAME_SEPARATOR = '.'
    DEFAULT_WAIT_TIMEOUT = 60
    DEFAULT_POLL_INTERVAL = 0.25


    def __repr__(self):
        my_class = self.__class__.__name__
        base_class = self.__class__.__bases__[0].__name__
        return '<{}({}) (locator="{}")>'.format(
                my_class, base_class, self.locator)


    @property
    def default_locator(self):
        return None


    @property
    def _parent_locator(self):
        try:
            return self.parent.locator
        except AttributeError:
            return ''


    @property
    def locator(self):
        if self.default_locator:
            return self.default_locator
        elif self._chain:
            return '{}{}'.format(self._parent_locator, self._locator)
        else:
            return self._locator


    @property
    def webdriver(self):
        try:
            return self.parent.webdriver
        except AttributeError:
            error_msg = ('webdriver should be an instance of selenium'
                        + ' WebDriver, instead is "{}"').format(self._webdriver)
            assert isinstance(self._webdriver, WebDriver), error_msg
            return self._webdriver


    @property
    def logger(self):
        try:
            return self.parent.logger
        except AttributeError:
            if self._logger is None:
                return logging
            else:
                return self._logger


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
            return PageObjectBase.DEFAULT_ROOT_NAME
        except KeyError:
            return PageObjectBase.DEFAULT_NAME


    @property
    def full_name(self):
        try:
            if isinstance(self.parent.children, dict):
                return '{}{}{}'.format(self.parent.full_name, PageObjectBase.NAME_SEPARATOR, self.name)
            else:
                return '{}[{}]'.format(self.parent.full_name, str(self.index))
        except AttributeError:
            return self.name


    @property
    def _log_id_short(self):
        return 'page object "{}"'.format(self.name)


    @property
    def _log_id_long(self):
        return 'full name path: "{}", element: "{}"'.format(
                self.full_name, self.locator)

