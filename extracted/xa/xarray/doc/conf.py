import datetime
import inspect
import os
import pathlib
import subprocess
import sys
from contextlib import suppress
from textwrap import dedent, indent
import packaging.version
import sphinx_autosummary_accessors
import yaml
from sphinx.application import Sphinx
from sphinx.util import logging

import xarray

LOGGER = logging.getLogger("conf")

allowed_failures = set()

print("python exec:", sys.executable)
print("sys.path:", sys.path)

if "CONDA_DEFAULT_ENV" in os.environ or "conda" in sys.executable:
    print("conda environment:")
    subprocess.run([os.environ.get("CONDA_EXE", "conda"), "list"])
else:
    print("pip environment:")
    subprocess.run([sys.executable, "-m", "pip", "list"])

print(f"xarray: {xarray.__version__}, {xarray.__file__}")

with suppress(ImportError):
    import matplotlib

    matplotlib.use("Agg")

try:
    import cartopy  # noqa: F401
except ImportError:
    allowed_failures.update(
        [
            "gallery/plot_cartopy_facetgrid.py",
        ]
    )

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinxcontrib.mermaid",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "jupyter_sphinx",
    "nbsphinx",
    "sphinx_autosummary_accessors",
    "sphinx.ext.linkcode",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_inline_tabs",
    "sphinx_remove_toctrees",
]


extlinks = {
    "issue": ("https://github.com/pydata/xarray/issues/%s", "GH%s"),
    "pull": ("https://github.com/pydata/xarray/pull/%s", "PR%s"),
    "discussion": ("https://github.com/pydata/xarray/discussions/%s", "D%s"),
}

# sphinx-copybutton configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.{3,}: | {5,8}: "
copybutton_prompt_is_regexp = True

# NBSphinx configuration
nbsphinx_timeout = 600
nbsphinx_execute = "always"
nbsphinx_allow_errors = False
nbsphinx_requirejs_path = ""
#  png2x/retina rendering of figues in docs would also need to modify custom.css:
# https://github.com/spatialaudio/nbsphinx/issues/464#issuecomment-652729126
#  .rst-content .image-reference img {
#   max-width: unset;
#   width: 100% !important;
#   height: auto !important;
#  }
# nbsphinx_execute_arguments = [
#     "--InlineBackend.figure_formats=['png2x']",
# ]
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

You can run this notebook in a `live session <https://mybinder.org/v2/gh/pydata/xarray/doc/examples/main?urlpath=lab/tree/doc/{{ docname }}>`_ |Binder| or view it `on Github <https://github.com/pydata/xarray/blob/main/doc/{{ docname }}>`_.

.. |Binder| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/pydata/xarray/main?urlpath=lab/tree/doc/{{ docname }}
"""

# AutoDoc configuration
autosummary_generate = True
autodoc_typehints = "none"

# Napoleon configuration
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True
napoleon_type_aliases = {
    # general terms
    "sequence": ":term:`sequence`",
    "iterable": ":term:`iterable`",
    "callable": ":py:func:`callable`",
    "dict_like": ":term:`dict-like <mapping>`",
    "dict-like": ":term:`dict-like <mapping>`",
    "path-like": ":term:`path-like <path-like object>`",
    "mapping": ":term:`mapping`",
    "file-like": ":term:`file-like <file-like object>`",
    # special terms
    # "same type as caller": "*same type as caller*",  # does not work, yet
    # "same type as values": "*same type as values*",  # does not work, yet
    # stdlib type aliases
    "MutableMapping": "~collections.abc.MutableMapping",
    "sys.stdout": ":obj:`sys.stdout`",
    "timedelta": "~datetime.timedelta",
    "string": ":class:`string <str>`",
    # numpy terms
    "array_like": ":term:`array_like`",
    "array-like": ":term:`array-like <array_like>`",
    "scalar": ":term:`scalar`",
    "array": ":term:`array`",
    "hashable": ":term:`hashable <name>`",
    # matplotlib terms
    "color-like": ":py:func:`color-like <matplotlib.colors.is_color_like>`",
    "matplotlib colormap name": ":doc:`matplotlib colormap name <matplotlib:gallery/color/colormap_reference>`",
    "matplotlib axes object": ":py:class:`matplotlib axes object <matplotlib.axes.Axes>`",
    "colormap": ":py:class:`colormap <matplotlib.colors.Colormap>`",
    # xarray terms
    "dim name": ":term:`dimension name <name>`",
    "var name": ":term:`variable name <name>`",
    # objects without namespace: xarray
    "DataArray": "~xarray.DataArray",
    "Dataset": "~xarray.Dataset",
    "Variable": "~xarray.Variable",
    "DataTree": "~xarray.DataTree",
    "DatasetGroupBy": "~xarray.core.groupby.DatasetGroupBy",
    "DataArrayGroupBy": "~xarray.core.groupby.DataArrayGroupBy",
    "Grouper": "~xarray.groupers.Grouper",
    "Resampler": "~xarray.groupers.Resampler",
    # objects without namespace: numpy
    "ndarray": "~numpy.ndarray",
    "MaskedArray": "~numpy.ma.MaskedArray",
    "dtype": "~numpy.dtype",
    "ComplexWarning": "~numpy.ComplexWarning",
    # objects without namespace: pandas
    "Index": "~pandas.Index",
    "MultiIndex": "~pandas.MultiIndex",
    "CategoricalIndex": "~pandas.CategoricalIndex",
    "TimedeltaIndex": "~pandas.TimedeltaIndex",
    "DatetimeIndex": "~pandas.DatetimeIndex",
    "IntervalIndex": "~pandas.IntervalIndex",
    "Series": "~pandas.Series",
    "DataFrame": "~pandas.DataFrame",
    "Categorical": "~pandas.Categorical",
    "Path": "~~pathlib.Path",
    # objects with abbreviated namespace (from pandas)
    "pd.Index": "~pandas.Index",
    "pd.NaT": "~pandas.NaT",
}

autodoc_type_aliases = napoleon_type_aliases  # Keep both in sync

# mermaid config
mermaid_version = "11.6.0"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", sphinx_autosummary_accessors.templates_path]

# The master toctree document.
master_doc = "index"

remove_from_toctrees = ["generated/*"]
# The language for content autogenerated by Sphinx.
language = "en"

# General information about the project.
project = "xarray"
copyright = f"2014-{datetime.datetime.now().year}, xarray Developers"

# The short Y.M.D version.
v = packaging.version.parse(xarray.__version__)
version = ".".join(str(p) for p in v.release)

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "debug.ipynb", "**.ipynb_checkpoints"]


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output ----------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"
html_title = ""

html_context = {
    "github_user": "pydata",
    "github_repo": "xarray",
    "github_version": "main",
    "doc_path": "doc",
}

# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html#references
html_theme_options = {
    #"announcement":"🍾 <a href='https://github.com/pydata/xarray/discussions/8462'>Xarray is now 10 years old!</a> 🎉",
    "logo": {"image_dark": "https://docs.xarray.dev/en/stable/_static/logos/Xarray_Logo_FullColor_InverseRGB_Final.svg"},
    "github_url":"https://github.com/pydata/xarray",
    "show_version_warning_banner":True,
    "use_edit_page_button":True,
    "header_links_before_dropdown": 8,
    "navbar_align": "left",
    "footer_center":["last-updated"],
    # Instead of adding these to the header bar they are linked in 'getting help' and 'contributing'
    # "icon_links": [
    # {
    #     "name": "Discord",
    #     "url": "https://discord.com/invite/wEKPCt4PDu",
    #     "icon": "fa-brands fa-discord",
    # },
    # {
    #     "name": "X",
    #     "url": "https://x.com/xarray_dev",
    #     "icon": "fa-brands fa-x-twitter",
    # },
    # {
    #     "name": "Bluesky",
    #     "url": "https://bsky.app/profile/xarray.bsky.social",
    #     "icon": "fa-brands fa-bluesky",
    # },
    # ]
}
# pydata_sphinx_theme use_edit_page_button with github link seems better
html_show_sourcelink = False

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logos/Xarray_Logo_RGB_Final.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/logos/Xarray_Icon_Final.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["style.css"]


# configuration for sphinxext.opengraph
ogp_site_url = "https://docs.xarray.dev/en/latest/"
ogp_image = "https://docs.xarray.dev/en/stable/_static/logos/Xarray_Logo_RGB_Final.png"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta property="twitter:site" content="@xarray_dev" />',
    '<meta name="image" property="og:image" content="https://docs.xarray.dev/en/stable/_static/logos/Xarray_Logo_RGB_Final.png" />',
]

# Redirects for pages that were moved to new locations
rediraffe_redirects = {
    "terminology.rst": "user-guide/terminology.rst",
    "data-structures.rst": "user-guide/data-structures.rst",
    "indexing.rst": "user-guide/indexing.rst",
    "interpolation.rst": "user-guide/interpolation.rst",
    "computation.rst": "user-guide/computation.rst",
    "groupby.rst": "user-guide/groupby.rst",
    "reshaping.rst": "user-guide/reshaping.rst",
    "combining.rst": "user-guide/combining.rst",
    "time-series.rst": "user-guide/time-series.rst",
    "weather-climate.rst": "user-guide/weather-climate.rst",
    "pandas.rst": "user-guide/pandas.rst",
    "io.rst": "user-guide/io.rst",
    "dask.rst": "user-guide/dask.rst",
    "plotting.rst": "user-guide/plotting.rst",
    "duckarrays.rst": "user-guide/duckarrays.rst",
    "related-projects.rst": "user-guide/ecosystem.rst",
    "faq.rst": "get-help/faq.rst",
    "why-xarray.rst": "getting-started-guide/why-xarray.rst",
    "installing.rst": "getting-started-guide/installing.rst",
    "quick-overview.rst": "getting-started-guide/quick-overview.rst",
    "contributing.rst": "contribute/contributing.rst",
    "developers-meeting.rst": "contribute/developers-meeting.rst",
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = today_fmt

# Output file base name for HTML help builder.
htmlhelp_basename = "xarraydoc"


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "cftime": ("https://unidata.github.io/cftime", None),
    "cubed": ("https://cubed-dev.github.io/cubed/", None),
    "dask": ("https://docs.dask.org/en/latest", None),
    "flox": ("https://flox.readthedocs.io/en/latest/", None),
    "hypothesis": ("https://hypothesis.readthedocs.io/en/latest/", None),
    "iris": ("https://scitools-iris.readthedocs.io/en/latest", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "numba": ("https://numba.readthedocs.io/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "python": ("https://docs.python.org/3/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "sparse": ("https://sparse.pydata.org/en/latest/", None),
    "xarray-tutorial": ("https://tutorial.xarray.dev/", None),
    "zarr": ("https://zarr.readthedocs.io/en/stable/", None),
    "xarray-lmfit": ("https://xarray-lmfit.readthedocs.io/stable", None),
}

# based on numpy doc/source/conf.py
def linkcode_resolve(domain, info):
    """
    Determine the URL corresponding to Python object
    """
    if domain != "py":
        return None

    modname = info["module"]
    fullname = info["fullname"]

    submod = sys.modules.get(modname)
    if submod is None:
        return None

    obj = submod
    for part in fullname.split("."):
        try:
            obj = getattr(obj, part)
        except AttributeError:
            return None

    try:
        fn = inspect.getsourcefile(inspect.unwrap(obj))
    except TypeError:
        fn = None
    if not fn:
        return None

    try:
        source, lineno = inspect.getsourcelines(obj)
    except OSError:
        lineno = None

    if lineno:
        linespec = f"#L{lineno}-L{lineno + len(source) - 1}"
    else:
        linespec = ""

    fn = os.path.relpath(fn, start=os.path.dirname(xarray.__file__))

    if "+" in xarray.__version__:
        return f"https://github.com/pydata/xarray/blob/main/xarray/{fn}{linespec}"
    else:
        return (
            f"https://github.com/pydata/xarray/blob/"
            f"v{xarray.__version__}/xarray/{fn}{linespec}"
        )


def html_page_context(app, pagename, templatename, context, doctree):
    # Disable edit button for docstring generated pages
    if "generated" in pagename:
        context["theme_use_edit_page_button"] = False


def update_gallery(app: Sphinx):
    """Update the gallery page."""

    LOGGER.info("Updating gallery page...")

    gallery = yaml.safe_load(pathlib.Path(app.srcdir, "gallery.yml").read_bytes())

    for key in gallery:
        items = [
            f"""
         .. grid-item-card::
            :text-align: center
            :link: {item['path']}

            .. image:: {item['thumbnail']}
                :alt: {item['title']}
            +++
            {item['title']}
            """
            for item in gallery[key]
        ]

        items_md = indent(dedent("\n".join(items)), prefix="    ")
        markdown = f"""
.. grid:: 1 2 2 2
    :gutter: 2

    {items_md}
    """
        pathlib.Path(app.srcdir, f"{key}-gallery.txt").write_text(markdown)
        LOGGER.info(f"{key} gallery page updated.")
    LOGGER.info("Gallery page updated.")


def update_videos(app: Sphinx):
    """Update the videos page."""

    LOGGER.info("Updating videos page...")

    videos = yaml.safe_load(pathlib.Path(app.srcdir, "videos.yml").read_bytes())

    items = []
    for video in videos:
        authors = " | ".join(video["authors"])
        item = f"""
.. grid-item-card:: {" ".join(video["title"].split())}
    :text-align: center

    .. raw:: html

        {video['src']}
    +++
    {authors}
        """
        items.append(item)

    items_md = indent(dedent("\n".join(items)), prefix="    ")
    markdown = f"""
.. grid:: 1 2 2 2
    :gutter: 2

    {items_md}
    """
    pathlib.Path(app.srcdir, "videos-gallery.txt").write_text(markdown)
    LOGGER.info("Videos page updated.")


def setup(app: Sphinx):
    app.connect("html-page-context", html_page_context)
    app.connect("builder-inited", update_gallery)
    app.connect("builder-inited", update_videos)
