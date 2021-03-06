# -*- coding: utf-8 -*-
#
# F5 ML2 Driver for OpenStack documentation build configuration file, created by
# sphinx-quickstart on Wed Nov  8 10:31:07 2017.
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
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('./'))

import f5_sphinx_theme
import networking_f5

VERSION = networking_f5.__version__

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinxjp.themes.basicstrap',
    'cloud_sptheme.ext.table_styling',
    ]

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
project = u'F5 ML2 Driver for OpenStack'
copyright = u'2017, F5 Networks'
author = u'F5 Networks'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = VERSION
# The full version, including alpha/beta/rc tags.
release = VERSION

# OpenStack release
openstack_release = "Newton"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

suppress_warnings = ['image.nonlocal_uri']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'f5_sphinx_theme'
html_theme_path = f5_sphinx_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
                        #'site_name': 'F5 OpenStack Docs Home',
                        'next_prev_link': False
                     }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {'**': ['searchbox.html', 'localtoc.html', 'globaltoc.html']}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'F5 ML2 Driver for OpenStack'

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'F5-ML2-Driver-OpenStack_doc'


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
    (master_doc, 'F5-ML2-Driver-OpenStack_doc.tex', u'F5 ML2 Driver for OpenStack',
     u'F5 Networks', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'F5-ML2-Driver-OpenStack_doc', u'F5 ML2 Driver for OpenStack',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'F5-ML2-Driver-OpenStack_doc', u'F5 ML2 Driver for OpenStack',
     author, 'F5ML2DriverforOpenStack',
     'Documentation for the F5 ML2 Driver for OpenStack',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}

rst_epilog = '''
.. |agent| replace:: :code:`f5-openstack-agent`
.. |agent-long| replace:: F5 Agent for OpenStack Neutron
.. |driver| replace:: :code:`f5-openstack-lbaasv2-driver`
.. |driver-long| replace:: F5 Driver for OpenStack LBaaSv2
.. |ml2| replace:: F5 ML2 Driver
.. |ml2-long| replace:: F5 ML2 Driver for OpenStack
.. |ml2_pip_branch| replace:: git+https://github.com/F5Networks/f5-openstack-ml2-driver@v%(openstack_release_l)s
.. |ml2_pip_version| replace:: git+https://github.com/F5Networks/f5-openstack-ml2-driver@v%(version)s
.. |openstack| replace:: %(openstack_release)s
.. |release-notes| raw:: html

    <a class="btn btn-success" href="https://github.com/F5Networks/f5-openstack-ml2-driver/releases/tag/v%(version)s/">Release Notes</a>
.. _Agent-tenant affinity: http://clouddocs.f5.com/cloud/openstack/v1/lbaas/#agent-tenant-affinity
.. _available F5 Agent: %(baseurl)s/products/openstack/latest/agent/
.. _Configure and start the F5 Agent: %(baseurl)s/products/openstack/agent/latest/index.html#configure-the-agent-long
.. _F5 Agent configuration file: %(baseurl)s/products/openstack/agent/latest/
.. _F5 Agent for OpenStack Neutron: %(baseurl)s/products/openstack/agent/latest
.. _F5 Driver for OpenStack LBaaSv2: %(baseurl)s/products/openstack/lbaasv2-driver/latest
.. _F5 Integration for OpenStack Neutron: http://clouddocs.f5.com/cloud/openstack/latest/lbaas/index.html
.. _F5 LBaaSv2 Quick Reference: %(baseurl)s/cloud/openstack/latest/lbaas/quick-reference.html
.. _F5 Service Provider Package: %(baseurl)s/cloud/openstack/latest/lbaas-prep
.. _Neutron LBaaS API: https://wiki.openstack.org/wiki/Neutron/LBaaS/API_2.0
.. _OpenStack Neutron: https://docs.openstack.org/neutron/latest/config-file.html
.. _ML2 mechanism driver: https://wiki.openstack.org/wiki/Neutron/ML2#Mechanism_Drivers
.. _Partners: %(baseurl)s/cloud/openstack/latest/support/partners.html
''' % {
    'openstack_release': openstack_release,
    'openstack_release_l': openstack_release.lower(),
    'version': version,
    'baseurl': 'http://clouddocs.f5.com'
}
