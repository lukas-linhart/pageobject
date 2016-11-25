from .pageobjectbase import PageObjectBase


class Locator(object):

    def __init__(self, value, page_object=None):
        self._value = value
        assert isinstance(page_object, PageObjectBase)
        self._page_object = page_object


    @property
    def chain(self):
        return self._page_object._chain


    @property
    def parent_locator_value(self):
        try:
            return self._page_object._parent_locator.value
        except AttributeError:
            return ''


    @property
    def value(self):
        if self.chain:
            return '{}{}'.format(self.parent_locator_value, self._value)
        else:
            return self._value

