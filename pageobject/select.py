from .pageobject import PageObject
from selenium.webdriver.support.ui import Select as Python2IncompatibleSelect


class WebDriverSelect(Python2IncompatibleSelect, object):
    """
    This is a workaround for selenium.webdriver.support.ui.Select class
    not inheriting from object.
    """
    pass


class Select(PageObject):

    @property
    def _select_class(self):
        return WebDriverSelect


    @property
    def elem(self):
        return self._select_class(self.webelement)


    def __getattr__(self, attribute_name):
        return self.elem.__getattribute__(attribute_name)

