===========================
Naming conventions: boolean
===========================

Booleans should start with ``is_``, ``has_``, etc.

**BAD:**

.. rst-class:: bad

.. code-block:: python

    class User(object):

        def __init__(self, username, password, avatar):
            self.username = username
            self.password = password
            self.avatar = avatar

        def get_avatar_path(self):
            if self.avatar:
                return os.path.join('avatars', self.username + '.png')

    >>> user = User('admin', 'passwd', avatar=True)   # What the author meant.
    >>> user.avatar
    True
    >>> user.get_avatar_path()
    'avatars/admin.png'
    >>> user = User('admin', 'passwd', avatar=False)   # What the author meant.
    >>> user.avatar_path
    None
