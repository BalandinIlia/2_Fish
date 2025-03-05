import connexion
import six

from swagger_server import util

i = 0

def calc():
    global i
    i = i + 1
    return {"status": "OK"}, 500

def healthcheck():  # noqa: E501
    """healthcheck

    Standard server healthcheck # noqa: E501


    :rtype: None
    """
    return calc()
