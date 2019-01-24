# -*- coding: utf-8 -*-
#
# Graph Rigidity and Flexibility documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 15 11:10:03 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
#sys.path.append(os.path.join('.','ext'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'inventory_builder', 'multidocs','sage_autodoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks',
    'sphinx.ext.viewcode',
    'matplotlib.sphinxext.plot_directive']


mathjax_config = {
    'extensions': ['tex2jax.js'],
    'tex2jax': {
      'inlineMath': [ ['$','$'], ["\\(","\\)"]], # 
      #'displayMath': [ ['$$','$$'], ["\\[","\\]"] ],
      'processEscapes': True
      }
}

# This code is executed before each ".. PLOT::" directive in the Sphinx
# documentation. It defines a 'sphinx_plot' function that displays a Sage object
# through mathplotlib, so that it will be displayed in the HTML doc
plot_html_show_source_link = False
plot_pre_code = """
def sphinx_plot(plot):
    import matplotlib.image as mpimg
    from sage.misc.temporary_file import tmp_filename
    import matplotlib.pyplot as plt
    if os.environ.get('SAGE_SKIP_PLOT_DIRECTIVE', 'no') != 'yes':
        fn = tmp_filename(ext=".png")
        plot.plot().save(fn)
        img = mpimg.imread(fn)
        plt.imshow(img)
        plt.margins(0)
        plt.axis("off")
        plt.tight_layout(pad=0)

def sphinx_plot_list(plot_list, rows, columns):
    import matplotlib.image as mpimg
    from sage.misc.temporary_file import tmp_filename
    import matplotlib.pyplot as plt
    if os.environ.get('SAGE_SKIP_PLOT_DIRECTIVE', 'no') != 'yes':
        n = 1
        for plot in plot_list:
            plt.subplot(rows,columns,n)
            fn = tmp_filename(ext=".png")
            plot.plot().save(fn)
            img = mpimg.imread(fn)
            plt.imshow(img)
            plt.margins(0)
            plt.axis("off")
            plt.tight_layout(pad=0)
            n += 1
from sage.all_cmdline import *
"""


plot_html_show_formats = False



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Graph Rigidity and Flexibility'
copyright = u'2019, Jan Legerský'
author = u'Jan Legerský'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


extlinks = {
    'wikipedia': ('https://en.wikipedia.org/wiki/%s', 'Wikipedia article '),
    'arxiv': ('http://arxiv.org/abs/%s', 'Arxiv '),
    'oeis': ('https://oeis.org/%s', 'OEIS sequence '),
    'doi': ('https://dx.doi.org/%s', 'doi:')
    }

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
#html_theme_options = {}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GraphRigidityandFlexibilitydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GraphRigidityandFlexibility.tex', u'Graph Rigidity and Flexibility Documentation',
     u'Jan Legerský', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'graphrigidityandflexibility', u'Graph Rigidity and Flexibility Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GraphRigidityandFlexibility', u'Graph Rigidity and Flexibility Documentation',
     author, 'GraphRigidityandFlexibility', 'One line description of project.',
     'Miscellaneous'),
]

