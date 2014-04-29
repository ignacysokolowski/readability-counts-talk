===========
Punctuation
===========

Space after comma, full stop, colon, etc.

::

    foo(1,2)  # Bad.
    foo(1.2)
    foo(1, 2)

    foo(one, two,three, four)  # Bad.
    foo(one, two.three, four)
    foo(one, two, three, four)

    [1,2,3,4,5,6,7]  # Bad.
    [1,2,3,4.5,6,7]  # Bad.
    [1, 2, 3, 4, 5, 6, 7]
    [1, 2, 3, 4.5, 6, 7]
