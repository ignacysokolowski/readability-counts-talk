============================
Naming conventions: function
============================

Function or method name should be lowercase.

**BAD:**

.. rst-class:: bad

::

    def Request(url):
        pass

    request = Request('http://...')   # What the user expects.
    response = Request('http://...')  # What the author meant.

**GOOD:**

::

    def request(url):
        pass

    response = request('http://...')
