==============================
Nesting statements in one line
==============================

.. code-block:: json

    [
      {"title": "foo bar", "body": "Lorem ipsum ..."},
      {"title": "bar foo", "body": "Dolor sit amet ..."}
    ]


**BAD:**

.. rst-class:: bad

::

    def get_first_initial_bad(file_path):
        return json.loads(open(file_path).read())[0]['title'][0].upper()
