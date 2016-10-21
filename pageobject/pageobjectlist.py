from .pageobjectbase import PageObjectBase
from .pageobject import PageObject
from selenium.common.exceptions import StaleElementReferenceException


class PageObjectList(PageObjectBase):

    def __init__(self, locator, parent, chain=True, name=None, children_class=None, children_locator=None, count_locator=None):
        self._locator = locator
        self.parent = parent
        self._chain = chain
        self._name = name
        self._children_class = children_class
        self._children_locator = children_locator
        self._count_locator = count_locator

        try:
            self.parent.register_child(self)
        except AttributeError:
            pass


    def __bool__(self):
        return bool(len(self))


    def __getitem__(self, slice):
        return self.children[slice]


    def __len__(self):
        return len(self.children)


    @property
    def children(self):
        children_count = len(self.webdriver.find_elements_by_xpath(self.count_locator))
        children = []
        for i in range(children_count):
            locator = self.children_locator.format(i+1)
            ChildrenClass = self.children_class
            child = ChildrenClass(locator, self, chain=False)
            child.index = i
            children.append(child)
        return children


    @property
    def children_class(self):
        if self._children_class:
            return self._children_class
        else:
            return PageObject


    @property
    def default_children_locator(self):
        return None


    @property
    def children_locator(self):
        if self.default_children_locator:
            return self.default_children_locator
        elif self._children_locator:
            return self._children_locator
        else:
            return '({})[{}]'.format(self.locator, '{}')


    @property
    def default_count_locator(self):
        return None


    @property
    def count_locator(self):
        if self.default_count_locator:
            return self.default_count_locator
        elif self._count_locator:
            return self._count_locator
        else:
            return self.locator


    def index(self, value, attempt=1):
        if attempt == 1:
            self.logger.info('getting index of "{}" within {}'.format(value, self._log_id_short))
        self.logger.debug('getting index of "{}" within page object, attempt number {}; {}'.format(value, attempt, self._log_id_long))
        try:
            index = [item.text for item in self[:]].index(value)
            self.logger.info('index of "{}" within {} is {}'.format(value, self._log_id_short, index))
            self.logger.debug('index of "{}" within page object is {}; {}'.format(value, index, self._log_id_long))
            return index
        except StaleElementReferenceException:
            self.logger.debug('getting index failed, trying again')
            return self.index(value, attempt=attempt+1)

