==================================
Indentation of an ``if`` statement
==================================

**BAD:**

.. rst-class:: bad

::

    if (self.foo(some_argument) and
        self.bar(another_argument) and
        self.baz(third_argument) and
        self.spam(fourth_argument)):
        self.foobar(some_argument)

* The last line looks like another condition for the ``if`` statement.

**GOOD:**

::

    if (self.foo(some_argument) and
            self.bar(another_argument) and
            self.baz(third_argument) and
            self.spam(fourth_argument)):
        self.foobar(some_argument)

* Indented twice.
