==============================
Nesting statements in one line
==============================

.. code-block:: json

    [
      {"title": "foo bar", "body": "Lorem ipsum ..."},
      {"title": "bar foo", "body": "Dolor sit amet ..."}
    ]

**GOOD:**

::

    def get_first_initial_good(file_path):
        with open(file_path) as f:
            json_content = f.read()
        articles = json.loads(json_content)
        first_article = articles[0]
        title = first_article['title']
        first_letter = title[0]
        initial = first_letter.upper()
        return initial
