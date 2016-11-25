from .pageobjectbase import PageObjectBase


class Locator(object):

    def __init__(self, *args, **kwargs):
        self._value = args[0]
        self.page_object = kwargs['page_object']
        assert isinstance(self.page_object, PageObjectBase)


    @property
    def chain(self):
        return self.page_object._chain


    @property
    def parent_locator_value(self):
        try:
            return self.page_object._parent_locator.value
        except AttributeError:
            return ''


    @property
    def value(self):
        if self.chain:
            return '{}{}'.format(self.parent_locator_value, self._value)
        else:
            return self._value

