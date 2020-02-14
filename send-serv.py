import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import glob


try:
    print("Azure Blob storage v12 - Python quickstart sample")
    # Quick start code goes here
    # Retrieve the connection string for use with the application. The storage
    # connection string is stored in an environment variable on the machine
    # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
    # created after the application is launched in a console or with Visual Studio,
    # the shell or application needs to be closed and reloaded to take the
    # environment variable into account.
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = str("abc")
    # Create the container
    #container_client = blob_service_client.create_container(container_name,)

    # Create a file in local Documents directory to upload and download
    local_path = "C:/Users/kkang/Documents/GitHub/faceapi/images"
    images = glob.glob(local_path+'/*.jpg') #bring all jpg files in the folder
    for i in images:
        local_file_name = str(i)
        upload_file_path = os.path.join(local_path, local_file_name)
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)
