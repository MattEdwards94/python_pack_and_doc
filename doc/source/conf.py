# -*- coding: utf-8 -*-
#
# Pack and Doc documentation build configuration file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
from __future__ import print_function

# Make sure that we create docs for the built version of Pack and Doc, not
# the installed version
import pack_and_doc
import sys
import glob
import os

script_dir = os.path.dirname(__file__)
build_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "build"))

build_paths = glob.glob(f"{build_dir}/*/pack_and_doc")

for path in build_paths:
    dir, name = os.path.split(path)
    sys.path.insert(0, dir)

print(f"PYTHONPATH = {sys.path}")

# Now import pack_and_doc, when we have a correct path

# -- General configuration -----------------------------------------------
# Add any Sphinx extension module names here, as strings.
# They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinxcontrib.programoutput',
    'sphinx_issues',
]

# Github repo
issues_github_path = 'chryswoods/python_pack_and_doc'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Pack and Doc'
copyright = u'2020 University of Bristol'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

branch = os.getenv("PACK_AND_DOC_BRANCH", None)

if branch is None:
    version = pack_and_doc.__version__.split("+")[0]
    # The full version, including alpha/beta/rc tags.
    release = pack_and_doc.__version__
    branch = pack_and_doc.__branch__
    revisionid = pack_and_doc.__revisionid__
    repository = pack_and_doc.__repository__
else:
    version = os.getenv("PACK_AND_DOC_VERSION")
    release = os.getenv("PACK_AND_DOC_RELEASE")
    revisionid = os.getenv("PACK_AND_DOC_REVISIONID")
    repository = os.getenv("PACK_AND_DOC_REPOSITORY")

print(f"repository = {repository}")
print(f"branch = {branch}")
print(f"revisionid = {revisionid}")
print(f"version = {version} : RELEASE = {release}")

# Replace all "|PackAndDocVersion|" with the version number
rst_epilog = f".. |PackAndDocVersion| replace:: {version}"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '*_test*']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "autolink"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- options for mathjax
# note there is no protocol given here to avoid mixing http with https
# see: http://docs.mathjax.org/en/latest/start.html#secure-cdn-access
mathjax_path = ("https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?"
                "config=TeX-AMS-MML_HTMLorMML")

# -- Options for HTML output ---------------------------------------------

# theme
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    'style_nav_header_background': ''
}
# pngmath_latex_preamble = r"""
# \usepackage{color}
# \definecolor{textgray}{RGB}{51,51,51}
# \color{textgray}
# """
# pngmath_use_preview = True
# pngmath_dvipng_args = ['-gamma 1.5', '-D 96', '-bg Transparent']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Pack and Doc Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Pack and Doc"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/logo.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicons/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']
html_js_files = ['custom.js']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {'**': ['sourcelink.html', 'globaltoc.html']}


# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'PackAndDocDoc'


# -- Options for LaTeX output --------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r"\usepackage{amsmath,amssymb}",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'PackAndDoc.tex', u'Pack and Doc Documentation',
     u'Michel Lab', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'PackAndDoc', u'Pack and Doc Documentation',
     [u'University of Bristol'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'PackAndDoc', u'Pack and Doc Documentation',
     u'University of Bristol', 'PackandDoc'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

autosummary_generate = True
autodoc_default_options = {
    'members': None,  # Include all members (methods).
    'special-members': None,
    'exclude-members': '__dict__,__weakref__'  # Exclude "standard" methods.
}

# spell checking
spelling_lang = 'en_US'
spelling_word_list_filename = 'spelling_wordlist.txt'
spelling_show_suggestions = True


# try to exclude deprecated
def skip_deprecated(app, what, name, obj, skip, options):
    if hasattr(obj, "func_dict") and "__deprecated__" in obj.func_dict:
        print("skipping " + name)
        return True
    return skip or False


def setup(app):
    app.connect('autodoc-skip-member', skip_deprecated)
    try:
        from sphinx.ext.autosummary import Autosummary
        from sphinx.ext.autosummary import get_documenter
        from docutils.parsers.rst import directives
        from sphinx.util.inspect import safe_getattr
        import re

        class AutoAutoSummary(Autosummary):

            option_spec = {
                'methods': directives.unchanged,
                'attributes': directives.unchanged
            }

            required_arguments = 1

            @staticmethod
            def get_members(obj, typ, include_public=None):
                if not include_public:
                    include_public = []
                items = []
                for name in dir(obj):
                    try:
                        documenter = get_documenter(
                            app, safe_getattr(obj, name), obj)
                    except AttributeError:
                        continue
                    if documenter.objtype == typ:
                        items.append(name)
                public = [
                    x for x in items if x in include_public or not x.startswith('_')]
                return public, items

            def run(self):
                clazz = self.arguments[0]
                try:
                    (module_name, class_name) = clazz.rsplit('.', 1)
                    m = __import__(module_name, globals(),
                                   locals(), [class_name])
                    c = getattr(m, class_name)
                    if 'methods' in self.options:
                        _, methods = self.get_members(
                            c, 'method', ['__init__'])

                        self.content = ["~%s.%s" % (
                            clazz, method) for method in methods if not method.startswith('_')]
                    if 'attributes' in self.options:
                        _, attribs = self.get_members(c, 'attribute')
                        self.content = ["~%s.%s" % (
                            clazz, attrib) for attrib in attribs if not attrib.startswith('_')]
                finally:
                    return super(AutoAutoSummary, self).run()

        app.add_directive('autoautosummary', AutoAutoSummary)
    except BaseException as e:
        raise e


# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
