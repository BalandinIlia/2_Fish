import connexion
import six
import boto3

# Create an S3 client
s3 = boto3.client("s3")

# Specify your bucket and object
bucket_name = "temporalal"
object_key = "python_message.txt"

from swagger_server import util

i = 0

def calc():
    global i
    i = i + 1
    s3.put_object(bucket_name, python_message, "Hello, S3!")
    return {"status": "OK"}, 200

def healthcheck():  # noqa: E501
    """healthcheck

    Standard server healthcheck # noqa: E501


    :rtype: None
    """
    return calc()
