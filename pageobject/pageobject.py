from .singlepageobjectbase import SinglePageObjectBase
from . import commands


class PageObject(SinglePageObjectBase):

    def __init__(self, locator, chain=True, webdriver=None, logger=None, name=None):
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()


    # commands
    webelement = commands.webelement
    text = commands.text
    is_existing = commands.is_existing
    is_visible = commands.is_visible
    is_enabled = commands.is_enabled
    wait_until = commands.wait_until
    wait_for_exist = commands.wait_for_exist
    wait_for_vanish = commands.wait_for_vanish
    wait_for_visible = commands.wait_for_visible
    wait_for_enabled = commands.wait_for_enabled
    click = commands.click
    clear = commands.clear
    get_value = commands.get_value
    set_value = commands.set_value
    get_attribute = commands.get_attribute
    move_to = commands.move_to
    send_keys = commands.send_keys

