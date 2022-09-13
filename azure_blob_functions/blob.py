from azure.storage.blob import BlobServiceClient
from os import getenv

BlobServiceClient.from_connection_string(getenv("AZURE_STORAGE_CONNECTION_STRING"))