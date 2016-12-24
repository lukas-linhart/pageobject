def is_visible(self, log=True):
    """
    DEPRECATED! Return True if page object is visible, False otherwise.

    :param bool log: whether to log or not (default is True)
    :returns: whether page object is visible
    :rtype: bool
    """
    self.logger.warning('"is_visible" command is deprecated, use "is_displayed" instead!')
    return self.is_displayed(log=log)

