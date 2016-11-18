from .pageobjectbase import PageObjectBase
from . import commands


class PageObjectListBase(PageObjectBase):

    def __bool__(self):
        return bool(len(self))


    def __getitem__(self, slice):
        return self.children[slice]


    def __len__(self):
        return len(self.children)


    def _get_child_name(self, child_po):
        return '{}[{}]'.format(self.name, child_po.index)


    def _get_child_full_name(self, child_po):
        return '{}[{}]'.format(self.full_name, child_po.index)


    @property
    def _descendants(self):
        return self.children_class(None)._descendants


    # commands
    index = commands.index

