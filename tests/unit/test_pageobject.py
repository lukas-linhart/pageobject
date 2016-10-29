from pageobject import PageObject
import pytest


def test_dunder_bool_method_returns_True_when_is_existing(monkeypatch):
    po = PageObject('', None)
    monkeypatch.setattr(po, 'is_existing', lambda log=False: True)
    assert bool(po)


def test_dunder_bool_method_returns_False_when_is_not_existing(monkeypatch):
    po = PageObject('', None)
    monkeypatch.setattr(po, 'is_existing', lambda log=False: False)
    assert(bool(po) == False)

