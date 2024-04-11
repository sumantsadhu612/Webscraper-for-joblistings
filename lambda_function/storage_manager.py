# This file contains functions to manage job listings storage using AWS S3.

import json
import boto3
from botocore.exceptions import ClientError

S3_BUCKET_NAME = 'your-s3-bucket-name'
S3_FILE_NAME = 'job_listings.json'

def save_job_listings(job_listings):
    """
    Saves job listings to AWS S3.
    """
    s3 = boto3.resource('s3')
    try:
        s3.Object(S3_BUCKET_NAME, S3_FILE_NAME).put(Body=json.dumps(job_listings))
    except ClientError as e:
        print(f"Error saving job listings to S3: {e}")

def load_job_listings():
    """
    Loads job listings from AWS S3.
    """
    s3 = boto3.resource('s3')
    try:
        obj = s3.Object(S3_BUCKET_NAME, S3_FILE_NAME).get()
        job_listings = json.loads(obj['Body'].read())
        return job_listings
    except ClientError as e:
        print(f"Error loading job listings from S3: {e}")
        return []
