from datasette import hookimpl
from functools import wraps

PAGE = """
<html><title>410 Gone</title>
<style>body { padding: 1em; font-family: sans-serif; }</style>
<body>
<h1>410 Gone</h1>\n<p>This resource is no longer available.</p>
</body></html>
"""



@hookimpl
def asgi_wrapper(datasette):
    def wrap_with_http_gone(app):
        @wraps(app)
        async def http_gone(scope, receive, send):
            # Check if the request type is HTTP
            if scope.get("type") == "http":
                # Send an HTTP 410 Gone response
                await send({
                    "type": "http.response.start",
                    "status": 410,
                    "headers": [("content-type", "text/html")],
                })
                await send({
                    "type": "http.response.body",
                    "body": PAGE.encode("utf-8"),
                })
            else:
                # For non-HTTP requests, proceed as normal
                await app(scope, receive, send)

        return http_gone

    return wrap_with_http_gone
