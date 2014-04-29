==============================
Use namespaces: import modules
==============================

It's often a better idea to import module instead of each name directly.

**BAD:**

.. rst-class:: bad

::

    from requests import get, post, Session, session, HTTPError, Response

    # Somewhere at the bottom of a long module:
    session = Session()
    get(foo)

.. rst-class:: bad

::

    from requests import request

    def some_django_view(request):  # Overriding 'request'.
        response = request('POST', 'http://...')
