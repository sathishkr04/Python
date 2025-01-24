import logging
import boto3
import os
import json,requests
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

def disable_block_public_access(bucket_name):
    """Disable Block Public Access for the bucket."""
    try:
        s3_client = boto3.client('s3')
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
        logging.info(f"Disabled block public access for bucket '{bucket_name}'.")
        return True
    except ClientError as e:
        logging.error(f"Error disabling block public access: {e}")
        return False

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

def upload_file(file_name, bucket_name, object_name=None,content_type='text/html'):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client = boto3.client('s3')
        s3_client.upload_file(
            file_name, 
            bucket_name, 
            object_name, 
            ExtraArgs={'ContentType': content_type}
        )
        logging.info(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}' with content type '{content_type}'.")
    except ClientError as e:
        logging.error(f"Failed to upload file: {e}")
        return False
    return True

def enable_static_website_hosting(bucket_name):
    """Enable static website hosting for the S3 bucket."""
    try:
        s3_client = boto3.client('s3')
        s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration={
                'IndexDocument': {'Suffix': 'index.html'},
            }
        )
        logging.info(f"Static website hosting enabled for bucket '{bucket_name}'.")
        logging.info(f"Website URL: http://{bucket_name}.s3-website-{s3_client.meta.region_name}.amazonaws.com")
    except ClientError as e:
        logging.error(f"Error enabling static website hosting: {e}")
        return False
    return True
def scraping_website():
    url = input("Enter the valid website url: ")
    try:
        response = requests.get(url)
        response.raise_for_status() 
        with open("/workspaces/Python/index.html", 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML content of {url} has been saved to index.html")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# Main script
if __name__ == "__main__":
    bucket_name = "sathishkr"
    region = "us-east-1"

    # Step 1: Create Bucket
    if create_bucket(bucket_name, region):
        list_buckets()  # Verify bucket creation
        
        # Step 2: Set Bucket Policy
        if disable_block_public_access(bucket_name):
            if set_bucket_policy(bucket_name):
                # Step 3: Upload a file
                file_path = "/workspaces/Python/index.html"  # Replace with the path to your file
                if not os.path.exists(file_path):
                    logging.error(f"File not found: {file_path}")
                    exit(1)
                if upload_file(file_path, bucket_name):
                    logging.info("File uploaded successfully.")
                else:
                    logging.error("File upload failed.")
            else:
                logging.error("Failed to set bucket policy.")
        else:
            logging.error("Bucket creation failed.")
        # Enable static website hosting
        if enable_static_website_hosting(bucket_name):
            logging.info("Static website hosting configured successfully.")
        else:
            logging.error("Failed to configure static website hosting.")
        scraping_website()