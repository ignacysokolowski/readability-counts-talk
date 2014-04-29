==================
Group your imports
==================

**BAD:**

.. rst-class:: bad

::

    from django.shortcuts import render_to_response
    import datetime
    import requests  # Is requests in the standard library?
    from django.views.generic.list_detail import object_detail
    from .utils import something
    import os
