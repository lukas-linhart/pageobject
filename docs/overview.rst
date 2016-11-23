Overview
========

* :ref:`what-is-po`
* :ref:`what-is-po-design-pattern`
* :ref:`features`



.. _what-is-po:

What is pageobject
------------------

`Pageobject`_ library implements the so-called *Page Object design pattern*
on steroids. This library/implementation will be henceforth referred to as
``pageobject``.

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

Consider a simple ``login_page`` with only a few components.
Compare the nested model of the UI to the flat one::

    login_page
    ├── top_panel
    │   ├── logo
    │   │   └── is_visible()
    │   └── search_form
    │       ├── input
    │       │   ├── get_value()
    │       │   └── set_value()
    │       └── submit_button
    │           ├── is_enabled()
    │           └── click()
    └── login_form
        ├── username
        │   ├── get_value()
        │   └── set_value()
        ├── password
        │   ├── get_value()
        │   └── set_value()
        └── submit_button
            ├── is_enabled()
            └── click()

    login_page
    ├── is_logo_visible()
    ├── get_search_input_value()
    ├── set_search_input_value()
    ├── is_submit_search_button_enabled()
    ├── click_submit_search_button()
    ├── get_username_value()
    ├── set_username_value()
    ├── get_password_value()
    ├── set_password_value()
    ├── is_submit_login_button_enabled()
    └── click_submit_login_button()

In the above example, both structures provide the same methods,
just named differently, e.g. ``search_form.submit_button.click()`` vs.
``click_submit_search_button()`` or ``login_form.submit_button.click()``
vs. ``click_submit_login_button()``.

Apart from being a feature in itself, the nesting has several implications
which other features are based upon.

After closer inspection, it becomes immediately obvious that each
page object is a separate `namespace`_. This is crucial because not only
you don't need to worry about conflicting names (``submit_button`` within
``search_form`` is different from ``submit_button`` within ``login_form``),
but also each page object can inherit methods like ``click()``
from common base class and you don't need to reimplement and come up with
some crazy name for it. In fact, even the ``submit_button`` can be
a reusable component, because semantically it is and does the same
thing, just in a different context (the context being location of the
button webelement in the `DOM`_ of the webpage; more on that later).

.. _namespace: https://en.wikipedia.org/wiki/Namespace
.. _DOM: https://en.wikipedia.org/wiki/Document_Object_Model

