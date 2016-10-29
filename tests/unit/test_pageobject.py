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


def test_dunder_getitem_method_raises_KeyError_for_nonexisting_child():
    po = PageObject('', None)
    with pytest.raises(KeyError):
        po['nonexisting_child']

def test_dunder_getitem_method_returns_correct_child():
    root_po = PageObject('', None)
    child_po = PageObject('', None)
    root_po.child_po = PageObject('', root_po)
    assert root_po['child_po'] == root_po.child_po


def test_dunder_len_method_returns_correct_length():
    root_po = PageObject('', None)
    root_po.a = PageObject('', root_po)
    root_po.b = PageObject('', root_po)
    assert len(root_po) == len(root_po.children)

