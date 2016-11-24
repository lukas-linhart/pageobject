class Locator(object):

    def __init__(self, *args, **kwargs):
        self._value = args[0]


    @property
    def value(self):
        return self._value

