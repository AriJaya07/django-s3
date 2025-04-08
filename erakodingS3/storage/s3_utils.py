import os
import boto3
import mimetypes
from dotenv import load_dotenv

load_dotenv

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET = os.getenv("AWS_STORAGE_BUCKET_NAME")

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_file(file):
    file_name = file.name
    content_type, _ = mimetypes.guess_type(file.name)
    content_type = content_type or 'application/octet-stream'

    s3.upload_fileobj(file, AWS_STORAGE_BUCKET, file_name, ExtraArgs={
        'ContentType': content_type
    })

    region = s3.get_bucket_location(Bucket=AWS_STORAGE_BUCKET).get('LocationConstraint', 'us-east-1')
    return f"https://s3-{region}.amazonaws.com/{AWS_STORAGE_BUCKET}/{file_name.replace(' ', '+')}"

def delete_file(file_name):
    s3.delete_object(Bucket=AWS_STORAGE_BUCKET, Key=file_name)