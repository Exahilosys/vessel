# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import pkg_resources

sys.path.insert(0, os.path.abspath('..'))

project = 'vessel'
author = 'Exahilosys'
copyright = f'2023, {author}'

resource = pkg_resources.get_distribution(project)

release = resource.version


extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',
    'sphinx_paramlinks',
]

autodoc_member_order = 'bysource'

autodoc_default_options = {
    'show-inheritance': True
}

intersphinx_mapping = {
    'py': ('https://docs.python.org/3', None),
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

paramlinks_hyperlink_param = 'name'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']