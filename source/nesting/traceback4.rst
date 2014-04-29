==============================
Nesting statements in one line
==============================

.. code-block:: json

    null

**BAD:**

::

    Traceback (most recent call last):
      File "./initial.py", line 7, in get_first_initial_bad
        return json.loads(open(file_path).read())[0]['title'][0].upper()
    TypeError: 'NoneType' object has no attribute '__getitem__'

* Which is ``None``?  The JSON object or the title?

**GOOD:**

::

    Traceback (most recent call last):
      File "./initial.py", line 14, in get_first_initial_good
        first_article = articles[0]
    TypeError: 'NoneType' object has no attribute '__getitem__'
