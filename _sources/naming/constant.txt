============================
Naming conventions: constant
============================

Constants should be UPPERCASE.

**BAD:**

.. rst-class:: bad

.. code-block:: python

    from django.conf.settings import TimeZone

    time_zone = TimeZone('UTC')  # What the user expects.
    >>> TimeZone                 # What the author meant.
    'UTC'

**GOOD:**

.. code-block:: python

    from django.conf.settings import TIME_ZONE

    >>> TIME_ZONE
    'UTC'
