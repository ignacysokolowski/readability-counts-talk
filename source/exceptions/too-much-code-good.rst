===================================
Too much code in the ``try`` clause
===================================

**GOOD:**

.. code-block:: python

    try:
        user = find_user(email)
    except EmailError:
        self.log_failure(email)
    else:
        message = EmailMessage(from=user.email, subject='Foo', body='Bar')
        message.send(recipient_email)
    return {'user_email': email, 'recipient_email': recipient_email}
