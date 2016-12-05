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
    def _initialized_type(self):
        """
        :returns: type representation of the initialized value
        :rtype: str
        """
        val = self._initialized_value
        if val.startswith('#') or val.startswith('id='):
            return 'id'
        elif (val.startswith('(') or val.startswith('/') or
                val.startswith('./') or val.startswith('../') or
                val.startswith('*/')):
            return 'xpath'
        else:
            return 'unknown'


    @property
    def _chain(self):
        """
        Return whether to chain to the parent locator.

        :returns: whether to chain to the parent locator
        :rtype: bool
        """
        if self._initialized_type == 'id':
            return False
        else:
            return self._page_object._chain


    @property
    def _parent_locator_value(self):
        """
        Return value of the parent page object locator.

        :returns: value of the parent page object locator
        :rtype: str
        """
        return self._page_object._parent_locator_value


    def _id_to_xpath(self, initialized_value):
        """
        :param str value: initialized value of the locator
        :returns: id value converted to xpath
        :rtype: str
        """
        if initialized_value.startswith('#'):
            id_value = initialized_value[1:].strip()
        elif initialized_value.startswith('id='):
            id_value = initialized_value[3:].strip()
        return "//*[@id='{}']".format(id_value)


    @property
    def _xpath(self):
        """
        :returns: xpath value
        :rtype: str
        """
        if self._initialized_type == 'id':
            return self._id_to_xpath(self._initialized_value)
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
        if self._chain:
            return '{}{}'.format(self._parent_locator_value, self._xpath)
        else:
            return self._xpath

