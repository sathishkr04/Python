import logging
import boto3,os,json
from botocore.exceptions import ClientError

def create_bucket(bucket_name="sathishkr", region="us-east-1"):
    # Create bucket
    try:
        if region == "us-east-1":
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

# Create a bucket policy
bucket_name = "sathishkr"
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

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)

# Configure logging
# logging.basicConfig(level=logging.INFO)

# Uploading a file
def upload_file(file_name="/workspaces/Python/index.html", bucket="sathishkr", object_name="/workspaces/Python/index.html"):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        logging.info(f"Successfully uploaded {file_name} to {bucket}/{object_name}")
    except ClientError as e:
        logging.error(f"Failed to upload {file_name} to {bucket}/{object_name}: {e}")
        return False
    return True

# Usage example
if upload_file('myfile.txt', 'my-bucket'):
    logging.info("Upload was successful!")
else:
    logging.error("Upload failed!")
