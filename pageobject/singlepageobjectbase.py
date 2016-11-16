from .pageobjectbase import PageObjectBase


class SinglePageObjectBase(PageObjectBase):

    def __bool__(self):
        return self.is_existing(log=False)


    def __getitem__(self, key):
        return self.children[key]


    def __len__(self):
        return len(self.children)


    def __setattr__(self, attr_name, attr_value):
        object.__setattr__(self, attr_name, attr_value)
        if attr_name is not '_parent' and isinstance(attr_value, PageObjectBase):
            child = attr_value
            child.__dict__['_parent'] = self


    def init_children(self): # pragma: no cover
        """
        Meant to be overloaded by page objects
        containing other page objects.
        """
        pass


    @property
    def children(self):
        return {attr_name: attr_value for attr_name, attr_value in self.__dict__.items()
                if isinstance(attr_value, PageObjectBase)
                and attr_value is not self.parent}


    def _get_child_name(self, child_po):
        for child_name in self.children:
            if self.__dict__[child_name] == child_po:
                return child_name


    def _get_child_full_name(self, child_po):
        return '{}{}{}'.format(self.full_name, PageObjectBase.NAME_SEPARATOR,
                child_po.name)

