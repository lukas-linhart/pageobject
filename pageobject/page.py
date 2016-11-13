from .pageobjectbase import PageObjectBase
from . import commands


class Page(PageObjectBase):

    def __init__(self, url=None, locator='', chain=True, webdriver=None, logger=None, name=None):
        self._url = url
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()


    def load(self):
        self.webdriver.get(self._url)


    # commands
    is_existing = commands.is_existing
    wait_for_exist = commands.wait_for_exist
    wait_for_vanish = commands.wait_for_vanish

