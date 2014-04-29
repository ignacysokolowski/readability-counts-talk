==========================
Naming conventions: module
==========================

Module name should be lowercase.

**BAD:**

.. rst-class:: bad

::

    import os.Path

    path = os.Path('/tmp/foo.json')  # What the user expects.
    os.Path.exists('/tmp/foo.json')  # What the author meant.

**GOOD:**

::

    import os.path

    os.path.exists('/tmp/foo.json')
