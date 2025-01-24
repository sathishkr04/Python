import logging
import boto3
import os
import json
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def create_bucket(bucket_name, region="us-east-1"):
    """Create an S3 bucket in the specified region."""
    try:
        s3_client = boto3.client('s3', region_name=region)
        if region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        logging.info(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        logging.error(f"Error creating bucket: {e}")
        return False
    return True

def list_buckets():
    """List all existing S3 buckets."""
    try:
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        logging.info("Existing buckets:")
        for bucket in response.get('Buckets', []):
            logging.info(f"  {bucket['Name']}")
    except ClientError as e:
        logging.error(f"Error listing buckets: {e}")

def set_bucket_policy(bucket_name):
    """Set a public-read bucket policy for the given bucket."""
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': f'arn:aws:s3:::{bucket_name}/*'
        }]
    }

    # Convert the policy to a JSON string
    policy_string = json.dumps(bucket_policy)

    # Apply the bucket policy
    try:
        s3_client = boto3.client('s3')
        s3_client.put_bucket_policy(Bucket=bucket_name, Policy=policy_string)
        logging.info(f"Bucket policy applied to '{bucket_name}'.")
    except ClientError as e:
        logging.error(f"Error setting bucket policy: {e}")
        return False
    return True

def upload_file(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(file_name, bucket_name, object_name)
        logging.info(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}'.")
    except ClientError as e:
        logging.error(f"Failed to upload file: {e}")
        return False
    return True

# Main script
if __name__ == "__main__":
    bucket_name = "sathishkr"
    region = "us-east-1"

    # Step 1: Create Bucket
    if create_bucket(bucket_name, region):
        list_buckets()  # Verify bucket creation

        # Step 2: Set Bucket Policy
        if set_bucket_policy(bucket_name):
            # Step 3: Upload a file
            file_path = "myfile.txt"  # Replace with the path to your file
            if upload_file(file_path, bucket_name):
                logging.info("File uploaded successfully.")
            else:
                logging.error("File upload failed.")
        else:
            logging.error("Failed to set bucket policy.")
    else:
        logging.error("Bucket creation failed.")
