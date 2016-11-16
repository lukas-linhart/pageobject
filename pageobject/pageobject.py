from .singlepageobjectbase import SinglePageObjectBase


class PageObject(SinglePageObjectBase):

    def __init__(self, locator, chain=True, webdriver=None, logger=None, name=None):
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()

