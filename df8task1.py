from google.cloud import storage
import os

# Replace with your own credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'df8new.json'
project_id ='crypto-trail-369705'
bucket_name = 'data-fellowhip-8'
source_file_name = 'unnamed.jpg'
destination_blob_name = 'Test'
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client(project_id)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
upload_blob(bucket_name,source_file_name,destination_blob_name)