from pageobject import PageObject
import pytest


def test_dunder_repr_returns_correct_string(monkeypatch):
    locator = "//body"
    po = PageObject(locator, None)
    monkeypatch.setattr(PageObject, 'locator', locator)
    assert repr(po) == '<PageObject(PageObjectBase) (locator="{}")>'.format(
            locator)


def test_default_locator_returns_None_when_not_provided():
    po = PageObject('', None)
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

