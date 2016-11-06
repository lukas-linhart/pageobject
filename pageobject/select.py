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
    def elem(self):
        return WebDriverSelect(self.webelement)


    @property
    def _delegated_attributes(self):
        return {
            'options',
            'all_selected_options',
            'first_selected_option',
            'select_by_value',
            'select_by_index',
            'select_by_visible_text',
            'deselect_all',
            'deselect_by_value',
            'deselect_by_index',
            'deselect_by_visible_text',
        }


    def __getattr__(self, attribute_name):
        if attribute_name in self._delegated_attributes:
            return self.elem.__getattribute__(attribute_name)
        else:
            return object.__getattribute__(self, attribute_name)

