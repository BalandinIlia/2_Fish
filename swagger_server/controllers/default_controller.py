import connexion
import six
import boto3
import sys

# Create an S3 client
#s3 = boto3.client("s3")

# Specify your bucket and object
#bucket_name = "temporalal"
#object_key = "python_message.txt"

from swagger_server import util

i = 0

def calc():
    #print("This is an error message", file=sys.stderr)
    #global i
    #i = i + 1
    #response = s3.put_object(Bucket = bucket_name, Key = object_key, Body = "Hello, S3!".encode("utf-8"))
    #str = print(response)
    return {"status": str}, 200

def healthcheck():  # noqa: E501
    """healthcheck

    Standard server healthcheck # noqa: E501


    :rtype: None
    """
    return calc()
