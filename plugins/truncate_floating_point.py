from datasette import hookimpl


@hookimpl
def render_cell(column, value):
    if isinstance(value, float):
        # Try to avoid confusing 1.3890318e-07 syntax
        if value < 0.0001:
            return "{:.10f}".format(value)
        else:
            return round(value, 5)
