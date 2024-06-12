# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
def setup(app):
    app.add_css_file('css/custom.css')

project = 'Документация к Проекту'
project_copyright = 'Проекту'
copyright = '2024 г, ООО Проект'
author = 'Кравец М.А.'
version = '0.1.0'
release = '0.1.0'
plantuml = 'java -Djava.awt.headless=true -jar /usr/bin/plantuml.jar'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_dark_mode",
    "sphinx_copybutton",
    "sphinxcontrib.httpdomain",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.plantuml",
    "sphinx.ext.graphviz",
    "sphinxcontrib.openapi",
    'sphinxcontrib.redoc',
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'groundwork'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "body_max_width": "1200px",
}
html_static_path = ['_static']
html_css_files = [
    "css/custom.css"
]
html_output_encoding = 'utf-8'

graphviz_output_format = 'svg'
html_show_sourcelink = False

redoc = [
    {
        'name': 'Sample API',
        'page': 'api/redoc/sampleRedoc',
        'spec': 'api/openapi/sample_openapi.yaml',
        'embed': True,
        'opts': {
            'hide-hostname':True,
            'expand-responses': ["200", "201"],
        }
    },
]
