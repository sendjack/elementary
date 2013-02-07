"""
    xsrf
    ----

    Provide Singleton access for the xsrf token to the entire View.

    Note: This might not be necessary.

"""

_xsrf_token = None


def get_xsrf_token():
    """ Return the xsrf token. """
    return _xsrf_token


def set_xsrf_token(xsrf_token):
    """ Set the xsrf token. """
    global _xsrf_token
    _xsrf_token = xsrf_token
