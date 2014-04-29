==================
Readability Counts
==================

Slides from my talk on readability in Python.

http://ignacysokolowski.github.io/readability-counts-talk


Building the slides
===================

Install `Sphinx <http://sphinx-doc.org>`_ and
`Hieroglyph <http://docs.hieroglyph.io/en/latest/index.html>`_::

    $ pip install -r requirements.txt

After changing reStructuredText documents in the ``source`` directory, build
them using this command::

    $ make html

Slides will be available in ``index.html``.
