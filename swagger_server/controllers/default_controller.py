import connexion
import six

from swagger_server import util

i = 0

def calc():
    global i
    i = i + 1
    if(i%2 == 0):
        return {"status": "OK"}, 200
    else:
        return {"status": "NOT_OK"}, 500

def healthcheck():  # noqa: E501
    """healthcheck

    Standard server healthcheck # noqa: E501


    :rtype: None
    """
    return calc()
