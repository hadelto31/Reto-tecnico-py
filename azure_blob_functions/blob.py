from azure.storage.blob import BlobServiceClient
from os import getenv
from typing import BinaryIO

from responses.responses_json import responses_json

blob_service_client = BlobServiceClient.from_connection_string(getenv("AZURE_STORAGE_CONNECTION_STRING"))


def upload_blob(filename: str, container: str, data: BinaryIO):
    try:
        blob_client = blob_service_client.get_blob_client(container=container, blob=filename)

        blob_client.upload_blob(data)

        return responses_json(message="success")
    except Exception as e:
        return responses_json(message=e.message, status=500)


        
      