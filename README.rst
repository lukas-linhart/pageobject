==========
pageobject
==========

Page Object design pattern implementation built on top of selenium WebDriver.


How to install
==============

:code:`$ pip install pageobject`


What exactly is a page object ?
===============================

This implementation sticks to the notion that a page object can be not only
a web page but also any object on the page and each such page object can
contain another page objects.

The beauty of this approach lies in abstraction. When you have let's say
a ``login_page`` with multiple components (``top_banner``, ``main_menu``,
``login_form``, ``footer``, etc.), it makes better sense to deal with ``login_name``
and ``login_password`` inputs in the context of the ``login_form`` than
the context of the ``login_page`` itself. This simply follows the way a human
brain operates: When you think of a house, you will probably think of
a couple of walls, windows, a door, a roof, maybe a chimney and that's it.
A door knob or the color of the bathroom walls probably don't concern you
on this level.


How to use
==========

Interactive use
--------------

    >>> from selenium import webdriver
    >>> from pageobject import PageObject
    TODO



Script use
----------

