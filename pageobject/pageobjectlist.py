from .pageobject import PageObject


class PageObjectList(PageObject):

    @property
    def children(self):
        elems = self.webdriver.find_elements_by_xpath(self.locator)
        children = []
        for i, x in enumerate(elems):
            locator = '({})[{}]'.format(self.locator, str(i+1))
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


    def __getitem__(self, slice):
        return self.children[slice]


    def __len__(self):
        return len(self.children)


    def index(self, value):
        self.logger.info('getting index of "{}" within {}'.format(value, self._log_id_short))
        self.logger.debug('getting index of "{}" within page object; {}'.format(value, self._log_id_long))
        index = [item.text for item in self[:]].index(value)
        self.logger.info('index of "{}" within {} is {}'.format(value, self._log_id_short, index))
        self.logger.debug('index of "{}" within page object is {}; {}'.format(value, index, self._log_id_long))
        return index

