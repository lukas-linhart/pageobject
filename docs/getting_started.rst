Getting Started
===============

Installation
------------

Installation is straightforward with `pip`_ (`virtualenv`_ is recommended)::

    $ pip install pageobject

.. _pip: https://pip.pypa.io/en/stable/
.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/


Basic Interactive Use
---------------------

``pageobject`` can be used interactively to play around and build your page
object tree from scratch::

    >>> from selenium import webdriver # we still need selenium
    >>> from pageobject import Page, PageObject
    >>>
    >>> wd = webdriver.Chrome() # or any other browser
    >>> python_org = Page(url='http://www.python.org', webdriver=wd, name='python_org')
    >>> python_org.load()
    <Page(SinglePageObjectBase) (full_name="python_org")>
    >>> python_org.search_input = PageObject('#id-search-field')

