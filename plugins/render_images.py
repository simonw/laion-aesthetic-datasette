from datasette import hookimpl
from markupsafe import escape
from jinja2 import Markup

TEMPLATE = """
<a href="{url}" title="{url}">
  <img src="{url}" width="200" style="max-width: unset;" loading="lazy">
</a>
"""


@hookimpl
def render_cell(column, value):
    if column == "url" and value:
        return Markup(TEMPLATE.format(url=escape(value)))
