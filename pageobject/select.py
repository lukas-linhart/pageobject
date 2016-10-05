from .pageobject import PageObject
from selenium.webdriver.support.ui import Select as WebDriverSelect


class Select(PageObject):

    @property
    def elem(self):
        return WebDriverSelect(self.find())


    @property
    def options(self):
        return self.elem.options


    @property
    def all_selected_options(self):
        return self.elem.all_selected_options


    @property
    def first_selected_option(self):
        return self.elem.first_selected_option


    def select_by_value(self, value):
        self.elem.select_by_value(value)


    def select_by_index(self, index):
        self.elem.select_by_index(index)


    def select_by_visible_text(self, text):
        self.elem.select_by_visible_text(text)


    def deselect_all(self):
        self.elem.deselect_all()


    def deselect_by_value(self, value):
        self.elem.deselect_by_value(value)


    def deselect_by_index(self, index):
        self.elem.deselect_by_index(index)


    def deselect_by_visible_text(self, text):
        self.elem.deselect_by_visible_text(text)

