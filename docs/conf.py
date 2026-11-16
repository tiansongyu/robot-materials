"""Sphinx project documentation configuration."""
project = '机器人材料学：从选材到制造'
language = 'zh_CN'
extensions = ['sphinx_rtd_theme', 'myst_nb', 'sphinxcontrib.mermaid', 'sphinx.ext.mathjax']
html_theme = 'sphinx_rtd_theme'
html_title = project
html_short_title = project
html_theme_options = {
    'navigation_depth': 3,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'style_external_links': True,
}
html_static_path = ['_static']
html_css_files = ['custom.css']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_show_sourcelink = True
html_show_copyright = False
nitpicky = True

# MyST-NB registers MyST Markdown itself; do not also enable myst_parser.
myst_enable_extensions = ['dollarmath', 'colon_fence']
myst_heading_anchors = 3
nb_execution_mode = 'cache'
nb_execution_timeout = 60
nb_execution_raise_on_error = True
nb_execution_allow_errors = False
nb_execution_in_temp = True
mermaid_version = '11.12.2'
mermaid_init_config = {'startOnLoad': False, 'securityLevel': 'strict', 'theme': 'neutral'}
html_baseurl = 'https://tiansongyu.github.io/robot-materials/'
mermaid_use_local = 'vendor/mermaid/dist/mermaid.esm.min.mjs'
mathjax_path = 'vendor/mathjax/es5/tex-mml-chtml.js'
