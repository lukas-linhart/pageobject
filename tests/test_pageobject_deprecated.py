import os
import unittest
import sys

sys.path.insert(0, os.path.abspath('.'))

from pageobject import PageObject
from pageobject import PageObjectList


class PageObjectTests(unittest.TestCase):

    def test_PO_len_returns_number_of_children(self):
        root_po = PageObject('')
        root_po.nested_po = PageObject('', root_po)
        root_po.another_nested_po = PageObject('', root_po)
        self.assertEqual(len(root_po), len(root_po.children))

    def test_root_PO_has_correct_short_implicit_name(self):
        root_po = PageObject('', None)
        self.assertEqual(root_po.name, root_po.__class__.DEFAULT_ROOT_NAME)


    def test_root_PO_has_correct_short_explicit_name(self):
        po_name = 'explicit_name'
        root_po = PageObject('', None, name=po_name)
        self.assertEqual(root_po.name, po_name)


    def test_root_PO_has_the_same_short_and_full_name(self):
        root_po = PageObject('', None)
        self.assertEqual(root_po.name, root_po.full_name)


    def test_nested_PO_has_correct_short_implicit_name(self):
        root_po = PageObject('')
        root_po.nested_po = PageObject('')
        self.assertEqual(root_po.nested_po.name, 'nested_po')


    def test_nested_PO_has_correct_full_name(self):
        root_po, nested_po, leaf_po = (PageObject('') for x in range(3))
        root_po.nested_po = nested_po
        nested_po.leaf_po = leaf_po
        separator = PageObject.NAME_SEPARATOR
        leaf_po_full_name = '{}{}{}{}{}'.format(
                root_po.name, separator, nested_po.name,
                separator, leaf_po.name)
        self.assertEqual(leaf_po.full_name, leaf_po_full_name)


    def test_root_PO_has_correct_chained_locator(self):
        locator = '//body'
        root_po = PageObject(locator, chain=True)
        self.assertEqual(root_po._locator.value, locator)


    def test_root_PO_has_correct_nonchained_locator(self):
        locator = '//body'
        root_po = PageObject(locator, chain=False)
        self.assertEqual(root_po._locator.value, locator)


    def test_nested_PO_has_correct_chained_locator(self):
        root_po_locator = '//body'
        nested_po_locator = '//div'
        chained_locator = '{}{}'.format(root_po_locator, nested_po_locator)
        root_po = PageObject(root_po_locator)
        root_po.nested_po = PageObject(nested_po_locator, chain=True)
        self.assertEqual(root_po.nested_po._locator.value, chained_locator)


    def test_nested_PO_has_correct_nonchained_locator(self):
        root_po_locator = '//body'
        nested_po_locator = '//div'
        root_po = PageObject(root_po_locator)
        root_po.nested_po = PageObject(nested_po_locator, chain=False)
        self.assertEqual(root_po.nested_po._locator.value, nested_po_locator)



if __name__ == '__main__':
    unittest.main()

