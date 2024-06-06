# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'PyBDC'
copyright = '2023, Marupudi'
author = 'Harsha Marupudi'
release = '0.1'
version = '0.1.0'

python:
  install:
    - requirements: Doc/requirements.txt
    - method: pip
      
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]
html_theme = "sphinx_rtd_theme"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
