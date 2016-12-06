from pageobject import PageObject


def test_constructor_inits_parameters_correctly():
    locator = '//body'
    chain = 'chain'
    webdriver = 'webdriver'
    name = 'name'
    po = PageObject(locator, chain=chain, webdriver=webdriver, name=name)
    assert po._initialized_locator == locator
    assert po._parent == None
    assert po._chain == chain
    assert po._webdriver == webdriver
    assert po._name == name

def test_constructor_calls_init_children_method():
    class MockPageObject(PageObject):
        def init_children(self):
            self.children_initialized = True
    po = MockPageObject('')
    assert po.children_initialized is True

