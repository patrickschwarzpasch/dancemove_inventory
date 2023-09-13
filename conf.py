# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

project = 'dancemoves'
copyright = '2023, PaSch'
author = 'PaSch'
release = '2023-09-13'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_needs", "sphinxcontrib.plantuml",]

templates_path = ['_templates']
exclude_patterns = []

needs_id_regex = "^[A-Za-z0-9_]*"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
else:
    plantuml = 'java -jar %s' % os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar")

    plantuml_output_format = 'png'

needs_types = [
    # Architecture types
    {
        "directive": "int",
        "title": "Interface",
        "content": "plantuml",
        "prefix": "I_",
        "color": "#BFD8D2",
        "style": "card",
    },
    {
        "directive": "comp",
        "title": "Component",
        "content": "plantuml",
        "prefix": "C_",
        "color": "#BFD8D2",
        "style": "card",
    },
    {"directive": "sys", "title": "System", "content": "plantuml", "prefix": "S_", "color": "#BFD8D2", "style": "card"},
    # Normal types
    {"directive": "req", "title": "Requirement", "prefix": "R_", "color": "#BFD8D2", "style": "node"},
    {"directive": "spec", "title": "Specification", "prefix": "S_", "color": "#FEDCD2", "style": "node"},
    {"directive": "impl", "title": "Implementation", "prefix": "I_", "color": "#DF744A", "style": "node"},
    {"directive": "test", "title": "Test Case", "prefix": "T_", "color": "#DCB239", "style": "node"},
    {"directive": "feature", "title": "Feature", "prefix": "F_", "color": "#FFCC00", "style": "node"},
    {"directive": "user", "title": "User", "prefix": "U_", "color": "#777777", "style": "node"},
    {"directive": "action", "title": "Action", "prefix": "A_", "color": "#FFCC00", "style": "node"},
    {"directive": "milestone", "title": "Milestone", "prefix": "M_", "color": "#FF3333", "style": "node"},
    {"directive": "prep", "title": "Preparation", "prefix": "P_", "color": "#FF3333", "style": "node"},
]

needs_extra_links = [
    {
        "option": "blocks",
        "incoming": "is blocked by",
        "outgoing": "blocks",
        "copy": True,
        "style": "#AA0000",
        "style_part": "dotted,#AA0000",
        "style_start": "-",
        "style_end": "-o",
        "allow_dead_links": True,
    },
    {
        "option": "tests",
        "incoming": "is tested by",
        "outgoing": "tests",
        "copy": True,
        "style": "#00AA00",
        "style_part": "dotted,#00AA00",
    },
    {
        "option": "checks",
        "incoming": "is checked by",
        "outgoing": "checks",
        "copy": False,
        "style": "#00AA00",
        "style_part": "dotted,#00AA00",
    },
    {
        "option": "triggers",
        "incoming": "triggered by",
        "outgoing": "triggers",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
        "allow_dead_links": True,
    },
    {
        "option": "starts_with",
        "incoming": "triggers directly",
        "outgoing": "starts with",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "starts_after",
        "incoming": "triggers at end",
        "outgoing": "starts after",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "ends_with",
        "incoming": "triggers to end with",
        "outgoing": "ends with",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "follows_after",
        "incoming": "comes before",
        "outgoing": "follows after",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "has_direction",
        "incoming": "direction used in",
        "outgoing": "has direction",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
    {
        "option": "requires_preperation",
        "incoming": "preparation used in",
        "outgoing": "requires preperation",
        "copy": False,
        "style": "#00AA00",
        "style_part": "solid,#777777",
    },
]
