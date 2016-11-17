from .singlepageobjectbase import SinglePageObjectBase


class PageObject(SinglePageObjectBase):
    """
    Main general-purpose page object class.

    Extends :class:`SinglePageObjectBase`.
    """

    DEFAULT_ROOT_NAME = 'page_object'


    def __init__(self, locator, chain=True, webdriver=None, logger=None, name=None):
        """
        Create a page object and its children.

        :param string locator: Xpath describing position of the page
          object in the DOM.
        :param bool chain: Determines whether to chain locator
          to its parent.
        :param webdriver: Instance of selenium WebDriver.
        :type webdriver: :class:`selenium.webdriver.Remote` instance
        :param logger: Any object implementing the interface
          of the standard :module:`logging` module.
        :type logger: :module:`logging` or None
        :param string name: Name used when the page object is a root.
        """
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()

