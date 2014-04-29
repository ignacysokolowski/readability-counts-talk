===========
Name length
===========

Names should be descriptive but not too long.

**BAD:**

.. rst-class:: bad

.. code-block:: python

    class ArticleTitleCanNotBeLongerThan100CharactersError(Exception):
        pass

    from project.blog.exceptions import ArticleTitleCanNotBeLongerThan100CharactersError

**GOOD:**

.. code-block:: python

    class TitleLengthError(Exception):
        """Raised when article title is longer than 100 characters."""

    from project.blog.exceptions import TitleLengthError
    raise TitleLengthError("Title longer than 100 characters: %s", title)
