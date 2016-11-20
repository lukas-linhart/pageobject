==========
pageobject
==========

|docs|

Page Object design pattern implementation built on top of selenium WebDriver.

See the wiki_ for more detailed info.

.. _wiki: https://github.com/lukas-linhart/pageobject/wiki



How to install
==============

:code:`$ pip install pageobject`


How to use
==========

Interactive use
--------------

    >>> from selenium import webdriver
    >>> from pageobject import Page, PageObject
    >>> wd = webdriver.Chrome() # or any other browser
    >>> python_org = Page('http://www.python.org', webdriver=wd)
    >>> python_org.search_box = PageObject('//input')
    >>> python_org.load()
    >>> python_org.search_box.set_value('spam', press_enter=True)



Script use
----------


.. |docs| image:: https://readthedocs.org/projects/pageobject/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://pageobject.readthedocs.io/en/latest/?badge=latest

