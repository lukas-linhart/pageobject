import pytest
from pageobject import PageObject
from pageobject import PageObjectList


def test_PO_registers_as_child_of_another_po_via_attribute_assignment():
    root_po = PageObject('')
    nested_po = PageObject('')
    root_po.nested_po = nested_po
    assert 'nested_po' in root_po.children
    assert nested_po.parent is root_po


def test_POL_registers_as_child_of_a_po_via_attribute_assignment():
    root_po = PageObject('')
    nested_po_list = PageObjectList('')
    root_po.nested_po_list = nested_po_list
    assert 'nested_po_list' in root_po.children
    assert nested_po_list.parent is root_po

