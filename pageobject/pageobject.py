from .singlepageobjectbase import SinglePageObjectBase


class PageObject(SinglePageObjectBase):
    """Main general-purpose page object class."""

    DEFAULT_ROOT_NAME = 'page_object'
    """Default name for a root page object."""


    def __init__(self, locator, chain=True, webdriver=None, logger=None, name=None):
        """
        Create a page object and its children.

        :param str locator: Xpath describing location of the page
            object in the DOM.
        :param bool chain: Determines whether to chain locator
            to its parent.
        :param webdriver: Only needs to be provided for root page object.
        :param logger: Any object implementing the interface
            of the standard `logging` module.
        :param str name: Name used when the page object is a root.
        :type webdriver: :class:`selenium.webdriver.Remote` instance or None
        :type logger: `logging` or None

        :Example usage:

        .. code-block:: python

            from pageobject import PageObject
            top_panel = PageObject("//*[@class='topPanel']")

        """
        self._locator = locator
        self._chain = chain
        self._webdriver = webdriver
        self._logger = logger
        self._name = name
        self._parent = None

        self.init_children()

