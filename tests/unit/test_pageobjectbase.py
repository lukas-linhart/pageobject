import pytest
from pageobject import PageObject
from pageobject.pageobjectbase import PageObjectBase
from .fixtures import mock_po_base


def test_dunder_repr_returns_correct_string(monkeypatch, mock_po_base):
    monkeypatch.setattr(mock_po_base.__class__, 'locator', '//body')
    assert repr(mock_po_base) == '<MockPoBase(MockPoBaseTemplate) (locator="{}")>'.format(
            mock_po_base.locator)


def test_default_locator_returns_None_when_not_provided():
    po = PageObjectBase()
    assert po.default_locator is None


def test_locator_returns_default_locator_when_provided(monkeypatch):
    po = PageObject('', None)
    locator = 'default'
    monkeypatch.setattr(PageObject, 'default_locator', locator)
    assert po.locator == locator

def test_locator_returns_correct_value_when_not_chained(monkeypatch):
    locator = '//body'
    po = PageObject(locator, None)
    monkeypatch.setattr(po, '_chain', False)
    assert po.locator == locator

def test_locator_returns_correct_value_when_chained_and_parent_exists(monkeypatch):
    parent_locator = '//html'
    child_locator = '//body'
    class Parent:
        locator = parent_locator
    child_po = PageObject(child_locator, Parent)
    assert child_po.locator == '{}{}'.format(parent_locator, child_locator)

def test_locator_returns_correct_value_when_chained_but_not_a_child(monkeypatch):
    locator = '//body'
    po = PageObject(locator, None)
    monkeypatch.setattr(po, '_chain', True)
    assert po.locator == locator

