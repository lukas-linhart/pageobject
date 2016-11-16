from .singlepageobjectbase import SinglePageObjectBase
from . import commands


class Page(SinglePageObjectBase):

    DEFAULT_ROOT_NAME = 'page'


    def __init__(self, url=None, locator='', chain=True, webdriver=None, logger=None, name=None):
        self._url = url
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()


    # commands
    load = commands.load
    is_existing = commands.is_existing
    wait_for_exist = commands.wait_for_exist
    wait_for_vanish = commands.wait_for_vanish

