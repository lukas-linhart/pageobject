from .pageobjectlistbase import PageObjectListBase
from .pageobject import PageObject


class PageObjectList(PageObjectListBase):

    def __init__(self, locator, chain=True, children_class=None, children_locator=None, count_locator=None):
        self._locator = locator
        self._chain = chain
        self._children_class = children_class
        self._children_locator = children_locator
        self._count_locator = count_locator
        self._parent = None


    @property
    def _children_count(self):
        return len(self.webdriver.find_elements_by_xpath(self.count_locator))


    @property
    def children(self):
        children = []
        ChildrenClass = self.children_class
        for i in range(self._children_count):
            locator = self.children_locator.format(i+1)
            child = ChildrenClass(locator, chain=False)
            child.index = i
            child._parent = self
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

