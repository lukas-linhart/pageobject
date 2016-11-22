Overview
========

* :ref:`what-is-po`
* :ref:`what-is-po-design-pattern`
* :ref:`features`



.. _what-is-po:

What is pageobject
------------------

`Pageobject`_ library implements the so-called *Page Object design pattern*
on steroids. This implementation will be henceforth refered to as ``pageobject``.

.. _Pageobject: https://github.com/lukas-linhart/pageobject



.. _what-is-po-design-pattern:

What is Page Object design pattern
----------------------------------

In essence, Page Objects model the web application and serve
as an interface to actions that can be performed on and data
that can be retrieved from it.

In its simplest, traditional form, a Page Object is just a collection
of functions common to a web page to prevent repeating oneself.

While this is usually where the understanding of the Page Object design
pattern ends for many implementations, it is where it just starts
for ``pageobject``.



.. _features:

Features
--------

Nesting of page objects
~~~~~~~~~~~~~~~~~~~~~~~
``pageobject`` sticks to the notion that a page object can be not only
a web page but also any object on the page and each such page object
can contain another page objects.

The beauty of this approach lies in `abstraction`_ and simply follows
the way a human brain operates: When you think of an object, like
a house, you will probably think of a couple of walls, windows,
a door, a roof, maybe a chimney and that's it. A door knob or the color
of the bathroom walls probably don't concern you at this level.

.. _abstraction: https://en.wikipedia.org/wiki/Abstraction_(software_engineering)

