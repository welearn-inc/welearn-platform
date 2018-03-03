CORS_URLS_REGEX = r'^.*$' # CORS HEADERS ENBALED
CORS_ORIGIN_WHITELIST = (
    '*'
)

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)