from datasette import hookimpl


@hookimpl
def render_cell(column, value):
    if isinstance(value, float):
        # Truncate to 4 decimal places
        return "{0:.4g}".format(value)
