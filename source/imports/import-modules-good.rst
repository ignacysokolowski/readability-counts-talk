==============================
Use namespaces: import modules
==============================

It's often a better idea to import module instead of each name directly.

**GOOD:**

::

    import requests

    # Somewhere at the bottom of a long module:
    session = requests.Session()
    requests.get(foo)

::

    import requests

    def some_django_view(request):
        response = requests.request('POST', 'http://...')

::

    import pylons

    def do_something_using_pylons_config(config=None):
        config = config or pylons.config
