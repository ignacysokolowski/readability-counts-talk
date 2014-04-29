==============================
Nesting statements in one line
==============================

.. code-block:: json

    [{"title": ""}]

**BAD:**

::

    Traceback (most recent call last):
      File "./initial.py", line 7, in get_first_initial_bad
        return json.loads(open(file_path).read())[0]['title'][0].upper()
    IndexError: string index out of range

* Which one is a string?  The JSON object or the title?

**GOOD:**

::

    Traceback (most recent call last):
      File "./initial.py", line 16, in get_first_initial_good
        first_letter = title[0]
    IndexError: string index out of range
