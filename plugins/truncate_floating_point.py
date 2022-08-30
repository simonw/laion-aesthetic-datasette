from datasette import hookimpl


@hookimpl
def render_cell(column, value):
    if isinstance(value, float):
        return round(value, 5)
