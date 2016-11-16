from .pageobjectbase import PageObjectBase
from . import commands


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
        return '{}{}{}'.format(self.full_name, self.__class__.NAME_SEPARATOR,
                child_po.name)


    @property
    def _descendants(self):
        descendants = dict()
        for child_name, child in self.children.items():
            if not isinstance(child, SinglePageObjectBase):
                child_name = '{}[i]'.format(child_name)
            descendants[child_name] = child._descendants
        return descendants


    # commands
    webelement = commands.webelement
    text = commands.text
    is_existing = commands.is_existing
    is_visible = commands.is_visible
    is_enabled = commands.is_enabled
    wait_until = commands.wait_until
    wait_for_exist = commands.wait_for_exist
    wait_for_vanish = commands.wait_for_vanish
    wait_for_visible = commands.wait_for_visible
    wait_for_enabled = commands.wait_for_enabled
    click = commands.click
    clear = commands.clear
    get_value = commands.get_value
    set_value = commands.set_value
    get_attribute = commands.get_attribute
    move_to = commands.move_to
    send_keys = commands.send_keys

