import logging
from selenium.webdriver import Remote as WebDriver


class PageObjectBase(object):
    """
    Abstract page object base class.

    All the other classes inherit from this one.
    """

    DEFAULT_ROOT_NAME = 'root'
    """Default name for a root page object."""

    NAME_SEPARATOR = '.'
    """Separator character for long (chained) page object names."""

    DEFAULT_WAIT_TIMEOUT = 60
    """Default timeout (in seconds) for wait commands."""

    DEFAULT_POLL_INTERVAL = 0.25
    """Poll interval (in seconds) for wait commands."""


    def __nonzero__(self):      # pragma: no cover
        return self.__bool__()  # Python 2 throwback


    def __repr__(self):
        my_class = self.__class__.__name__
        base_class = self.__class__.__bases__[0].__name__
        try:
            locator = self.locator
        except: # pragma: no cover
            locator = 'INVALID LOCATOR'
        return '<{}({}) (locator="{}")>'.format(
                my_class, base_class, locator)


    @property
    def parent(self):
        """
        Return the parent of the page object.

        :returns: Parent page object.
        :rtype: :class:`pageobject.pageobjectbase.PageObjectBase` or `None` (default)
        """
        return self._parent


    @property
    def default_locator(self):
        """
        Return default locator, None by default.

        May be overridden to take precedence before the locator
        provided to constructor.

        :returns: default locator
        :rtype: `None` (default) or `str` (if overridden)
        """
        return None


    @property
    def _parent_locator(self):
        """
        Return the locator of the parent page object.

        :returns: locator of parent or empty string if parent does not exist
        :rtype: `str`
        """
        try:
            return self.parent.locator
        except AttributeError:
            return ''


    @property
    def locator(self):
        """
        Return the locator of the page object.

        If *chain* is True, chain the locator of the page object
        to the locator of its parent.

        :returns: locator of the page object
        :rtype: `str`
        """
        if self.default_locator:
            return self.default_locator
        elif self._chain:
            return '{}{}'.format(self._parent_locator, self._locator)
        else:
            return self._locator


    @property
    def webdriver(self):
        """
        Return the instance of WebDriver.

        If parent exists, use the webdriver property of the parent.
        Otherwise use the value provided to constructor.

        :returns: reference to the webdriver instance
        :rtype: `selenium.webdriver.Remote`
        :raises AssertionError: if the webdriver is not a valid WebDriver
        """
        try:
            return self.parent.webdriver
        except AttributeError:
            error_msg = ('webdriver should be an instance of selenium'
                        + ' WebDriver, instead is "{}"').format(self._webdriver)
            assert isinstance(self._webdriver, WebDriver), error_msg
            return self._webdriver


    @property
    def logger(self):
        """
        Return the logger object.

        :returns: standard logging module
        :rtype: :py:obj:`logging`
        """
        return logging


    @property
    def name(self):
        """
        Return name of the page object instance.

        If parent exists, ask for its child name, otherwise use the name
        provided to constructor. If that doesn't exist either,
        use `DEFAULT_ROOT_NAME`.

        :returns: Name of the page object.
        :rtype: `str`
        """
        try:
            return self.parent._get_child_name(self)
        except AttributeError:
            if self._name:
                return self._name
            else:
                return self.__class__.DEFAULT_ROOT_NAME


    @property
    def full_name(self):
        """
        Return full name of the page object instance.

        If parent exists, ask for its child full name, otherwiser use
        normal short name.

        :returns: Full name of the pge object.
        :rtype: `str`

        .. seealso::
            :py:func:`_get_child_full_name`

        """
        try:
            return self.parent._get_child_full_name(self)
        except AttributeError:
            return self.name


    @property
    def tree(self):
        """
        :returns: Hierarchical tree of page object and its descendants.
        :rtype: `dict`
        """
        return {self.name: self._descendants}


    @property
    def _log_id_short(self): # pragma: no cover
        """
        :returns: String identifying the page object by its name.
        :rtype: `str`
        """
        return 'page object "{}"'.format(self.name)


    @property
    def _log_id_long(self): # pragma: no cover
        """
        :returns: String identifying the page object
            by its full name and locator.
        :rtype: `str`
        """
        return 'full name path: "{}", element: "{}"'.format(
                self.full_name, self.locator)

