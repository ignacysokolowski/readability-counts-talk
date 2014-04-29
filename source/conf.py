# -*- coding: utf-8 -*-
"""Readability Counts slides build configuration file.

This file is execfile()d with the current directory set to its containing dir.

"""
# import sphinx_readable_theme


# -- General configuration ----------------------------------------------------

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Readability Counts'
copyright = u'2014, Ignacy Sokołowski'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

extensions = ['hieroglyph']
slide_theme_path = ['_themes']
slide_theme = 'readable'

# Output file base name for HTML help builder.
htmlhelp_basename = 'readabilitycountsdoc'


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(
    'index',
    project,
    project,
    [u'Ignacy Sokołowski'],
    1
)]
