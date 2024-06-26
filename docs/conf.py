# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import toml

sys.path.insert(0, os.path.abspath('..'))

project_config = toml.load('..//pyproject.toml')

# -- Project information -----------------------------------------------------

project = 'async-firebase-rest-api'
copyright = '2022, Asif Arman Rahman; 2024, Matias Kotlik'
author = 'Asif Arman Rahman, Matias Kotlik'

# The full version, including alpha/beta/rc tags
release = project_config['project']['version']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.intersphinx',
	'sphinx.ext.napoleon',
	'sphinx.ext.viewcode',
	'sphinx_design',
]

# auto section label configuration
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
	'google': ("https://googleapis.dev/python/google-auth/latest/", None),
	'google.cloud': ("https://googleapis.dev/python/storage/latest/", None),
	'google.cloud.firestore': ("https://googleapis.dev/python/firestore/latest/", None),
	'python': ("https://docs.python.org/3/", None),
	'requests': ("https://requests.readthedocs.io/en/stable/", None),
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# custom static css files to add
html_css_files = [
	"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/fontawesome.min.css",
	"css/my-styles.css",
]
