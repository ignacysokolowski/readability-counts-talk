========================================
Specify what exception you want to catch
========================================

.. code-block:: python
    :emphasize-lines: 4

    def find_user(username):
        try:
            user = Users.get(username)
        except UserLookupError:
            user = None
        return user
    >>> find_user('foo')
    <User foo>
    >>> find_user('bar')
    None
    >>> find_user(1)
    Traceback (most recent call last):
      File "api.py", line 7, in get
        username = username.lower()
    AttributeError: 'int' object has no attribute 'lower'

* We know that the user will be ``None`` when it's not found.
* We know what exception is raised when a user is not found.
* We know that we can catch other exceptions when calling ``find_user()``
* Avoid masking bugs.
