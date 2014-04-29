===================================
Use namespaces: never import ``*``!
===================================

**BAD:**

.. rst-class:: bad

::

    from requests import *
    from sqlalchemy.orm import *

    # Where do these come from?
    session = Session()
    get(foo)

**GOOD:**

::

    import requests
    import sqlalchemy.orm

    session = sqlalchemy.orm.Session()
    requests.get(foo)
