import logging
from selenium.webdriver import Remote as WebDriver


class PageObjectBase(object):

    DEFAULT_ROOT_NAME = 'root'
    NAME_SEPARATOR = '.'
    DEFAULT_WAIT_TIMEOUT = 60
    DEFAULT_POLL_INTERVAL = 0.25


    def __nonzero__(self):      # pragma: no cover
        return self.__bool__()  # Python 2 throwback


    def __repr__(self):
        my_class = self.__class__.__name__
        base_class = self.__class__.__bases__[0].__name__
        try:
            locator = self.locator
        except: # pragma: no cover
            locator = 'INVALID LOCATOR'
        return '<{}({}) (locator="{}")>'.format(
                my_class, base_class, locator)


    @property
    def parent(self):
        return self._parent


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
        try:
            return self.parent._get_child_name(self)
        except AttributeError:
            if self._name:
                return self._name
            else:
                return self.__class__.DEFAULT_ROOT_NAME


    @property
    def full_name(self):
        try:
            return self.parent._get_child_full_name(self)
        except AttributeError:
            return self.name


    @property
    def tree(self):
        return {self.name: self._descendants}


    @property
    def _log_id_short(self): # pragma: no cover
        return 'page object "{}"'.format(self.name)


    @property
    def _log_id_long(self): # pragma: no cover
        return 'full name path: "{}", element: "{}"'.format(
                self.full_name, self.locator)

