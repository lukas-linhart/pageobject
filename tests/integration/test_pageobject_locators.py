import pytest
from pageobject import PageObject
from pageobject import PageObjectList


def test_POL_child_locator_when_initialized_as_locator(monkeypatch):
    table = PageObject("//table")
    rows = PageObjectList("/rows")
    table.rows = rows
    children_count = 3
    index = 1
    monkeypatch.setattr(rows.__class__, '_children_count', children_count)
    assert rows.locator == "//table/rows"
    assert rows[index].locator == "(//table/rows)[{}]".format(index+1)


def test_POL_child_locator_when_initialized_as_children_locator(monkeypatch):
    table = PageObject("//table")
    rows = PageObjectList("/rows", children_locator="//rows[{}]")
    table.rows = rows
    children_count = 3
    index = 1
    monkeypatch.setattr(rows.__class__, '_children_count', children_count)
    assert rows.locator == "//table/rows"
    assert rows[index].locator == "//rows[{}]".format(index+1)


def test_POL_child_locator_when_provided_as_default_children_locator(monkeypatch):
    table = PageObject("//table")

    class Rows(PageObjectList):
        @property
        def default_children_locator(self):
            return "//rows[{}]"

    rows = Rows("/rows")
    table.rows = rows
    children_count = 3
    index = 1
    monkeypatch.setattr(rows.__class__, '_children_count', children_count)
    assert rows.locator == "//table/rows"
    assert rows[index].locator == "//rows[{}]".format(index+1)


def test_POL_count_locator_when_initialized_as_locator():
    table = PageObject("//table")
    rows = PageObjectList("//rows")
    table.rows = rows
    assert rows._count_locator_value == "//table//rows"


def test_POL_count_locator_when_initialized_as_count_locator():
    table = PageObject("//table")
    rows = PageObjectList("//rows", count_locator="//explicit_rows")
    table.rows = rows
    assert rows._count_locator_value == "//explicit_rows"


def test_POL_count_locator_when_provided_as_default_count_locator():
    table = PageObject("//table")

    class Rows(PageObjectList):
        @property
        def default_count_locator(self):
            return "//default_rows"

    rows = Rows("//rows")
    table.rows = rows
    assert rows._count_locator_value == "//default_rows"
