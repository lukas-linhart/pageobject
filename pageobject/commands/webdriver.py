from selenium.webdriver import Remote as WebDriver


@property
def webdriver(self):
    try:
        return self.parent.webdriver
    except AttributeError:
        error_msg = ('webdriver should be an instance of selenium'
                    + ' WebDriver, instead is "{}"').format(self._webdriver)
        assert isinstance(self._webdriver, WebDriver), error_msg
        return self._webdriver

