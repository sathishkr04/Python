import logging,os
from operation import create_bucket,list_buckets, disable_block_public_access, set_bucket_policy, upload_file, enable_static_website_hosting, scraping_website
from variables import bucket_name, region, file_path

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