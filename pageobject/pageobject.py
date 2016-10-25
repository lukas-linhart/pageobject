from .pageobjectbase import PageObjectBase
from . import commands


class PageObject(PageObjectBase):

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


    # commands
    webelement = commands.webelement
    text = commands.text
    is_existing = commands.is_existing
    is_visible = commands.is_visible
    wait_until = commands.wait_until
    wait_for_exist = commands.wait_for_exist
    wait_for_vanish = commands.wait_for_vanish
    wait_for_visible = commands.wait_for_visible
    click = commands.click
    clear = commands.clear
    get_value = commands.get_value
    set_value = commands.set_value
    get_attribute = commands.get_attribute
    move_to = commands.move_to
    send_keys = commands.send_keys

