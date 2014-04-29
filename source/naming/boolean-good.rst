===========================
Naming conventions: boolean
===========================

Booleans should start with ``is_``, ``has_``, etc.

**GOOD**:

.. code-block:: python

    class User(object):

        def __init__(self, username, password, has_avatar):
            self.username = username
            self.password = password
            self.has_avatar = has_avatar

        def get_avatar_path(self):
            if self.has_avatar:
                return os.path.join('avatars', self.username + '.png')

    >>> user = User('admin', 'passwd', has_avatar=True)
    >>> user.has_avatar
    True
    >>> user.get_avatar_path()
    'avatars/admin.png'
    >>> user = User('admin', 'passwd', has_avatar=False)
    >>> user.get_avatar_path()
    None
