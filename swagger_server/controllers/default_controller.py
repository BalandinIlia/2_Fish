import connexion
import six
import boto3
import sys

# Create an S3 client
s3 = boto3.client("s3")

# Specify your bucket and object
bucket_name = "temporalal"
object_key = "python_message.txt"

from swagger_server import util

def healthcheck():
    print("Logging: Performing standard healthcheck", file=sys.stderr)
    response = s3.put_object(Bucket = bucket_name, Key = object_key, Body = "Hello, S3!".encode("utf-8"))
    print("Logging: results of touching experimental bucket:", file=sys.stderr)
    print(print(response), file=sys.stderr)
    return {"status": "healthy"}, 200

def get_modules(organization_id: str, notebook_id: str):
    print(f"Processing get request for organization: {organization_id} and notebook: {notebook_id}.")
    modules = ["First module", f"Organization id: {organization_id}", f"Notebook id:{notebook_id}", "Fourth module"]
    return jsonify({"modules": modules}), 200
