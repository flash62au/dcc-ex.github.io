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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'DCC-EX Model Railroading'
copyright = '2020-2025 DCC-EX Team'
author = 'Fred Decker, Peter Akers, Peter Cole, Paul Antoine, Mani Kumar'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    # 'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.mathjax',
    # 'sphinx.ext.ifconfig',
    # 'sphinx.ext.viewcode',
    # 'sphinx.ext.graphviz',
    'sphinx_sitemap',
    # 'sphinx.ext.inheritance_diagram',
    'sphinxcontrib.spelling',
    'sphinx_toolbox.collapse',
    'ablog',
    'sphinx.ext.intersphinx',
    'sphinx_design',
    'sphinx_rtd_dark_mode',
    'sphinx_reredirects',
    # 'sphinx_last_updated_by_git',
    'notfound.extension',
    'linuxdoc.rstFlatTable'
]

autosectionlabel_prefix_document = True

# Don't make dark mode the user default
default_dark_mode = False

spelling_lang = 'en_UK'
tokenizer_lang = 'en_UK'
spelling_word_list_filename = ['spelling_wordlist.txt']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
]

# Set the default for literal blocks and code-block
highlight_language = 'none'

# Automatically number figure captions
numfig = True

numfig_format = {'figure': 'Fig %s:'}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "./_static/images/logo.png"

html_favicon = "./_static/images/favicon.ico"

# Added commented out lines below for 'titles_only' and 'navigation_depth'.
# If we wish to have the menu expand to lower levels than just page titles,
# uncomment these lines and comment the other option out to enable this in
# the menu.
html_theme_options = {
    'style_nav_header_background': 'white',
    'logo_only': True,
    # Toc options
    'includehidden': True,
    # 'titles_only': False,
    'titles_only': True,
    'collapse_navigation': False,
    # 'navigation_depth': 3
    'navigation_depth': -1
}

html_context = {
    'display_github': True,
    'github_user': 'DCC-EX',
    'github_repo': 'dcc-ex.github.io',
    'github_version': 'sphinx/docs/',
}

# leave this off to have todos invisible, set to true to render them and make the easy to see
# A list of all the todos in the document can be shown in the about page
todo_include_todos = True

# html_additional_pages = {
#     'exwebthrottle': 'exwebthrottle/index.html',
# }

html_css_files = [
    'css/dccex_theme.css',
    'css/big_picture_theme.css',
    'css/sphinx_design_overrides.css',
    # 'css/layout.css',
    # 'css/roundslider.min.css',
    # 'css/throttle.css' 
]

html_js_files = [
    'js/platform.js',
    'js/extra.js',
    # 'js/commandController.js',
    # 'js/exwebthrottle.js',
    # 'js/fnMaster.js',
    # 'js/jquery-3.2.1.min.js',
    # 'js/jquery-ui.min.js',
    # 'js/roundslider.min.js',
    # 'js/storageController.js'
]

# Sphinx sitemap
html_baseurl = 'https://dcc-ex.com/'
html_extra_path = [
  'robots.txt',
  ]

# ABlog options here
blog_path = 'news'
blog_title = 'DCC-EX News'
blog_baseurl = 'https://dcc-ex.com'
post_auto_excerpt = 1
post_auto_image = 0
blog_post_pattern = "news/posts/*"
blog_feed_fulltext = True
fontawesome_included = True

redirects = {
    "about/press/index": "../../about/about.html",
    "about/press/new-name": "https://dcc-ex.com/news/posts/20201001.html",
    "about/rewrite": "https://dcc-ex.com/news/posts/20201001.html",
    "advanced-setup/index": "../ex-commandstation/advanced-setup/index.html",
    "advanced-setup/supported-microcontrollers/index": "../../advanced-setup/supported-microcontrollers/index.html",
    "advanced-setup/supported-motorboards/index": "../../reference/hardware/motor-boards.html",
    "automation/EX-RAIL-intro": "../exrail/index.html",
    "automation/index": "../exrail/index.html",
    "developer-reference/api": "../reference/developers/api.html",
    "developer-reference/api": "../reference/developers/api.html",
    "developer-reference/index": "../reference/developers/index.html",
    "developer-reference/tech-reference": "../reference/developers/index.html",
    "download/commandstation": "ex-commandstation.html",
    "download/dcc-inspector-ex": "ex-dccinspector.html",
    "download/documents": "index.html",
    "download/schematics": "index.html",
    "download/turntable-ex": "ex-turntable.html",
    "downloads": "/download/index.html",
    "ex-commandstation/get-started/purchasing": "../diy/purchasing.html",
    "ex-commandstation/get-started/assembly": "../diy/assembly.html",
    "ex-commandstation/get-started/wifi-setup": "../diy/wifi-setup.html",
    "ex-commandstation/get-started/installer": "../installer-diy.html",
    "ex-commandstation/get-started/controllers": "../controllers-diy.html",
    "ex-commandstation/get-started/testing": "../testing-diy.html",
    "ex-commandstation/advanced-setup/supported-bluetooth/index": "../../../reference/hardware/bluetooth.html",
    "ex-commandstation/ready-to-run/index": "../rtr-index.html",
    "ex-commandstation/ready-to-run/connecting": "../rtr-connecting.html",
    "ex-commandstation/ready-to-run/manual": "../rtr-manual.html",
    "ex-commandstation/ready-to-run/purchasing": "../rtr-purchasing.html",
    "ex-commandstation/ready-to-run/wifi-setup": "../rtr-wifi-setup.html",
    "excsb1/quick-setup": "../ex-commandstation/rtr-connecting.html",
    "ex-csb1/quick-setup": "../../ex-commandstation/rtr-connecting.html",
    "csb1/quick-setup": "../ex-commandstation/rtr-connecting.html",
    "ex-installer/installing-original-installer": "index.html",
    "ex-rail/index": "../exrail/index.html",
    "ex-rail/deprecate-EX-RAIL-reference": "../exrail/index.html",
    "ex-rail/deprecate-EX-RAIL-summary": "../exrail/index.html",
    "ex-rail/about": "../exrail/about.html",
    "ex-rail/creating-elements": "../exrail/creating-elements.html",
    "ex-rail/EX-RAIL-command-reference": "../exrail/exrail-command-reference.html",
    "ex-rail/examples": "../exrail/examples.html",
    "ex-rail/getting-started": "../exrail/getting-started.html",
    "ex-rail/overview": "../exrail/overview.html",
    "ex-rail/tips": "../exrail/tips.html",
    "exwebthrottle/LICENSE": "../about/licence.html",
    "get-started/assembly": "../ex-commandstation/diy/assembly.html",
    "get-started/controllers": "../ex-commandstation/controllers-diy.html",
    "get-started/index": "../ex-commandstation/index.html",
    "get-started/installer": "../ex-commandstation/installer-diy.html",
    "get-started/levels": "../begin/levels.html",
    "get-started/wifi-setup": "../ex-commandstation/wifi-setup.html",
    "glossary": "./reference/glossary.html",
    "news/posts/20230310": "../../news.html",
    "news/posts/20230408": "../../news.html",
    "news/posts/20230806": "../../news.html",
    "press/index": "../../news.html",
    "press/v40-announce": "../../news.html",
    "reference/developers/tech-reference": "../../throttles/tech-reference.html",
    "reference/documents/decoder-table": "../../reference/hardware/decoder-list.html",
    "reference/hardware/bluetooth-boards": "../../reference/hardware/bluetooth.html",
    "reference/hardware/other/index": "../../reference/hardware/index.html",
    "reference/hardware/shopping-list": "../../ex-commandstation/purchasing.html",
    "reference/software/command-summary": "../../reference/software/command-summary-consolidated.html",
    "reference/software/command-reference": "../../reference/software/command-summary-consolidated.html",
    "reference/software/single-opcode-reference": "../../reference/software/command-summary-consolidated.html",
    "reference/software/index-dcpp-commands": "./command-summary-consolidated.html",
    "site-map/index": "../about/site-map.html",
    "support/create-ticket": "../support/index.html",
    "support/makerfabs-update-at-version-with-usb-to-ttl": "../support/wifi-at-version.html#correcting-the-at-version-on-a-makerfabs-esp8266-wifi-shield",
    "throttles/cab-engineer": "../throttles/software/cab-engineer.html",
    "throttles/hardware/physical-knobs": "../../throttles/hardware/engine-driver-physical-knobs.html",
    "throttles/physical-knobs": "../throttles/hardware/engine-driver-physical-knobs.html",
    "throttles/software/ex-webthrottle": "../../ex-webthrottle/index.html",
    "throttles/witcontroller": "../throttles/hardware/witcontroller.html",
    "throttles/withrottle": "../throttles/software/withrottle.html",
    "turntable-ex/index": "../ex-turntable/index.html",
    "turntable-ex/turntable-ex": "../ex-turntable/index.html",
    "under-development/track-manager": "../trackmanager/index.html",
}

# Configure sphinx-notfound-page
notfound_context = {
    "title": "Page Not Found",
    "body": """
<h1>Page Not Found</h1>

<p>Sorry, we couldn't find that page.</p>

<p>Try using the search box or go to the <a href="/index.html">homepage</a>.</p>
""",
}
notfound_urls_prefix = "/dcc-ex.github.io/"
