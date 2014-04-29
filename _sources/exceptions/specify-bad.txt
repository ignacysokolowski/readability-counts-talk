========================================
Specify what exception you want to catch
========================================

**BAD:**

.. rst-class:: bad

.. code-block:: python
    :emphasize-lines: 4

    def find_user(username):
        try:
            user = Users.get(username)
        except:
            user = None
        return user
    >>> find_user('foo')
    <User foo>
    >>> find_user('bar')
    None
    >>> find_user(1)
    None

* When the user will be ``None``?  When it's not found?  When the username is
  invalid?
* It will be ``None`` even when there's a bug in ``Users.get()``.
  Or somewhere deeper.
