from .singlepageobjectbase import SinglePageObjectBase


class PageObject(SinglePageObjectBase):

    DEFAULT_ROOT_NAME = 'page_object'


    def __init__(self, locator, chain=True, webdriver=None, logger=None, name=None):
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()

