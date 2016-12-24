def wait_for_visible(self, timeout=None):
    self.logger.warning('"wait_for_visible" command is deprecated, use "wait_until_displayed" instead!')
    self.wait_until_displayed(timeout=timeout)
    return self

