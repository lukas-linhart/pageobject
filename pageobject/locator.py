class Locator(object):
    """
    Locator provides representation of the locator of the page object.
    """

    def __init__(self, value, page_object=None):
        """
        Create a Locator object.

        :param str value: locator string
        :param page_object: reference to the page object instantiating
            the Locator
        """
        self._initialized_value = value
        self._page_object = page_object


    @property
    def chain(self):
        """
        Return whether to chain to the parent locator.

        :returns: whether to chain to the parent locator
        :rtype: bool
        """
        val = self._initialized_value
        if val.startswith('#') or val.startswith('id='):
            return False
        else:
            return self._page_object._chain


    @property
    def parent_locator_value(self):
        """
        Return value of the parent page object locator.

        :returns: value of the parent page object locator
        :rtype: str
        """
        return self._page_object._parent_locator_value


    @property
    def _xpath(self):
        """
        :returns: xpath value
        :rtype: str
        """
        val = self._initialized_value
        if val.startswith('#'):
            return "//*[@id='{}']".format(val[1:].strip())
        elif val.startswith('id='):
            return "//*[@id='{}']".format(val[3:].strip())
        else:
            return self._initialized_value


    @property
    def value(self):
        """
        Return final value of the locator:

        Chain the value to parent's value if applicable.

        :returns: final value of the locator
        :rtype: str
        """
        if self.chain:
            return '{}{}'.format(self.parent_locator_value, self._xpath)
        else:
            return self._xpath

