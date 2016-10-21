from . import useless_logger


class PageObjectBase(object):

    DEFAULT_NAME = 'page_object'
    DEFAULT_ROOT_NAME = 'root'
    NAME_SEPARATOR = '.'


    def __repr__(self):
        my_class = self.__class__.__name__
        base_class = self.__class__.__bases__[0].__name__
        return '<{}({}) (locator="{}")>'.format(
                my_class, base_class, self.locator)


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
            if self._logger is None:
                return useless_logger
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

