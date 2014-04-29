=========================
Naming conventions: class
=========================

Class name should be CamelCase.

**BAD:**

.. rst-class:: bad

::

    class request(object):
        pass

    response = request()  # What the user expects.
    request = request()   # What the author meant.

**GOOD:**

::

    class Request(object):
        pass

    request = Request()
