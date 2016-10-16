import os
import unittest
import sys
here = os.path.abspath(os.path.dirname(__file__))
parent_dir = '{}/..'.format(here)
sys.path.append(parent_dir)

import pageobject as po


class PageObjectTests(unittest.TestCase):

    def test_PO_children_property_returns_dict(self):
        root_po = po.PageObject('', None)
        self.assertIsInstance(root_po.children, dict)


    def test_root_PO_has_correct_short_implicit_name(self):
        root_po = po.PageObject('', None)
        self.assertEqual(root_po.name, po.PageObject.DEFAULT_ROOT_NAME)


    def test_root_PO_has_correct_short_explicit_name(self):
        po_name = 'explicit_name'
        root_po = po.PageObject('', None, name=po_name)
        self.assertEqual(root_po.name, po_name)


    def test_root_PO_has_the_same_short_and_full_name(self):
        root_po = po.PageObject('', None)
        self.assertEqual(root_po.name, root_po.full_name)


    def test_nested_PO_has_correct_short_implicit_name(self):
        root_po = po.PageObject('', None)
        root_po.nested_po = po.PageObject('', root_po)
        self.assertEqual(root_po.nested_po.name, 'nested_po')


    def test_nested_PO_has_correct_short_explicit_name(self):
        root_po = po.PageObject('', None)
        po_name = 'explicit_name'
        root_po.nested_po = po.PageObject('', root_po, name=po_name)
        self.assertEqual(root_po.nested_po.name, po_name)


    def test_nested_PO_has_correct_full_name(self):
        root_po = po.PageObject('', None)
        root_po.nested_po = po.PageObject('', root_po)
        correct_name = '{}.{}'.format(
                po.PageObject.DEFAULT_ROOT_NAME, root_po.nested_po.name)
        self.assertEqual(root_po.nested_po.full_name, correct_name)



if __name__ == '__main__':
    unittest.main()
