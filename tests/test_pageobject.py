import os
import unittest
import sys
here = os.path.abspath(os.path.dirname(__file__))
parent_dir = '{}/..'.format(here)
sys.path.append(parent_dir)

from pageobject import PageObject


class PageObjectTests(unittest.TestCase):

    def test_PO_children_property_returns_dict(self):
        root_po = PageObject('', None)
        self.assertIsInstance(root_po.children, dict)


    def test_PO_registers_as_child_via_attribute_assignment(self):
        root_po = PageObject('', None)
        nested_po = PageObject('', root_po)
        root_po.nested_po = nested_po
        self.assertIn('nested_po', root_po.children)


    def test_PO_registers_as_child_via_explicit_name(self):
        root_po = PageObject('', None)
        nested_po_name = 'nested_po'
        PageObject('', root_po, name=nested_po_name)
        self.assertIn(nested_po_name, root_po.children)


    def test_PO_getitem_returns_correct_child(self):
        root_po = PageObject('', None)
        root_po.nested_po = PageObject('', root_po)
        self.assertEqual(root_po['nested_po'], root_po.nested_po)


    def test_PO_len_returns_number_of_children(self):
        root_po = PageObject('', None)
        root_po.nested_po = PageObject('', root_po)
        root_po.another_nested_po = PageObject('', root_po)
        self.assertEqual(len(root_po), len(root_po.children))


    def test_root_PO_has_correct_short_implicit_name(self):
        root_po = PageObject('', None)
        self.assertEqual(root_po.name, PageObject.DEFAULT_ROOT_NAME)


    def test_root_PO_has_correct_short_explicit_name(self):
        po_name = 'explicit_name'
        root_po = PageObject('', None, name=po_name)
        self.assertEqual(root_po.name, po_name)


    def test_root_PO_has_the_same_short_and_full_name(self):
        root_po = PageObject('', None)
        self.assertEqual(root_po.name, root_po.full_name)


    def test_nested_PO_has_correct_short_implicit_name(self):
        root_po = PageObject('', None)
        root_po.nested_po = PageObject('', root_po)
        self.assertEqual(root_po.nested_po.name, 'nested_po')


    def test_nested_PO_has_correct_short_explicit_name(self):
        root_po = PageObject('', None)
        po_name = 'explicit_name'
        root_po.nested_po = PageObject('', root_po, name=po_name)
        self.assertEqual(root_po.nested_po.name, po_name)


    def test_nested_PO_has_correct_full_name(self):
        root_po = PageObject('', None)
        nested_po = PageObject('', root_po, name='nested_po')
        leaf_po = PageObject('', nested_po, name='leaf_po')
        separator = PageObject.NAME_SEPARATOR
        leaf_po_full_name = '{}{}{}{}{}'.format(
                root_po.name, separator, nested_po.name,
                separator, leaf_po.name)
        self.assertEqual(leaf_po.full_name, leaf_po_full_name)



if __name__ == '__main__':
    unittest.main()

