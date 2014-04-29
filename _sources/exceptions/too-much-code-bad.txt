===================================
Too much code in the ``try`` clause
===================================

**BAD:**

.. rst-class:: bad

.. code-block:: python

    try:
        user = find_user(email)
        message = EmailMessage(from=user.email, subject='Foo', body='Bar')
        message.send(recipient_email)
    except EmailError:
        self.log_failure(email)
    return {'user_email': email, 'recipient_email': recipient_email}

* Which line actually raises the ``EmailError``?
