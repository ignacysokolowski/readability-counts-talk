=======================================
Indentation of a dictionary, list, etc.
=======================================

**BAD:**

.. rst-class:: bad

::

    some_dictionary = {'ok': 200, 'not_found': 404, 'forbidden': 403,
                       'bad_request': 400, 'internal_server_error': 500}

.. code-block:: diff

    @@ -27,7 +27,6 @@
    - some_dictionary = {'ok': 200, 'not_found': 404, 'forbidden': 403,
    -                    'bad_request': 400, 'internal_server_error': 500}
    + some_dictionary = {'ok': 200, 'unauthorized': 401, 'not_found': 404, 
    +                    'forbidden': 403, 'bad_request': 400,
    +                    'internal_server_error': 500}

* What changed?  A key, a value?  A new item was added?
