import os
from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("daft-pgm").version
except DistributionNotFound:
    pass

# Support canonical URL
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
if os.environ.get("READTHEDOCS", "") == "True":
    html_context = {"READTHEDOCS": True}

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "myst_nb",
]

templates_path = ["_templates"]
master_doc = "index"

project = "Daft"
copyright = "2012-2021, Daft Developers"
version = __version__
release = __version__

exclude_patterns = ["_build"]
pygments_style = "sphinx"

html_theme = "daft"
html_theme_options = {
    "tagline": "Beautifully rendered probabilistic graphical models."
}
html_theme_path = ["_themes"]
html_static_path = ["_static"]
html_sidebars = {"**": ["relations.html", "searchbox.html"]}
html_show_sourcelink = False
htmlhelp_basename = "Daftdoc"
