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


def test_locator_returns_default_locator_when_provided(monkeypatch, mock_po_base):
    locator = 'default'
    monkeypatch.setattr(mock_po_base.__class__, 'default_locator', locator)
    assert mock_po_base.locator == locator

def test_locator_returns_correct_value_when_not_chained(monkeypatch, mock_po_base):
    locator = '//body'
    mock_po_base._chain = False
    mock_po_base._locator = locator
    assert mock_po_base.locator == locator

def test_locator_returns_correct_value_when_chained_and_parent_exists(mock_po_base):
    parent_locator = '//html'
    child_locator = '//body'
    class Parent:
        locator = parent_locator
    mock_po_base._chain = True
    mock_po_base._locator = child_locator
    mock_po_base.parent = Parent()
    assert mock_po_base.locator == '{}{}'.format(parent_locator, child_locator)

def test_locator_returns_correct_value_when_chained_but_not_a_child(monkeypatch, mock_po_base):
    locator = '//body'
    mock_po_base._chain = True
    mock_po_base._locator = locator
    mock_po_base.parent = None
    assert mock_po_base.locator == locator

