import os
import connexion
import six
import boto3
import sys

from swagger_server import util
from flask import jsonify

def healthcheck():
    print("Logging: Performing standard healthcheck", file=sys.stderr)
    return {"status": "healthy"}, 200

def buck_name():
    print(f"Logging: request bucket name started", file=sys.stderr)
    name = os.getenv('S3_BUCKET_NAME')
    print(f"Logging: Requested bucket name: {name}.", file=sys.stderr)
    return name

def list_files_with_prefix(bucket_name, prefix):
    print(f"Logging: Searching in bucket {bucket_name} for files with prefix {prefix}", file=sys.stderr)
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')

    all_files = []

    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        if 'Contents' in page:
            for obj in page['Contents']:
                all_files.append(obj['Key'])

    print(f"Logging: Found files: {all_files}", file=sys.stderr)
    return all_files

def get_modules(organization_id: str, notebook_id: str):
    print(f"Logging: Processing get request for organization: {organization_id} and notebook: {notebook_id}.", file=sys.stderr)
    modules = list_files_with_prefix(buck_name(), organization_id + '/' + notebook_id)
    print(f"Logging: Found modules: {modules}.", file=sys.stderr)
    sorted_modules = sorted(modules)
    print(f"Logging: Found modules after sorting: {sorted_modules}.", file=sys.stderr)
    if len(sorted_modules) == 0:
        return {"status": "Not Found"}, 404
    else:
        return jsonify({"modules": sorted_modules}), 200
