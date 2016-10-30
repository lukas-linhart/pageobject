from pageobject import PageObject


def test_dunder_repr_returns_correct_string():
    locator = "//body"
    po = PageObject(locator, None)
    assert repr(po) == '<PageObject(PageObjectBase) (locator="{}")>'.format(
            locator)

