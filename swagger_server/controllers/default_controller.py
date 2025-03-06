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
    # Upload a file
    s3.upload_file("requirements.txt", bucket_name, object_key)
    s3.upload_file("default_controller.py", bucket_name, object_key)
    return {"status": "OK"}, 200

def healthcheck():  # noqa: E501
    """healthcheck

    Standard server healthcheck # noqa: E501


    :rtype: None
    """
    return calc()
