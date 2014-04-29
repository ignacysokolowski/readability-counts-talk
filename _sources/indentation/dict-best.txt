=======================================
Indentation of a dictionary, list, etc.
=======================================

**BEST:**

::

    some_dictionary = {
        'ok': 200,
        'not_found': 404,
        'forbidden': 403,
        'bad_request': 400,
        'internal_server_error': 500,
    }

.. code-block:: diff

    @@ -27,7 +27,6 @@ some_dictionary = {
         'internal_server_error': 500,
    +    'conflict': 409,
     }
