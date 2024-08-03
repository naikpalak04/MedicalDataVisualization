from azure.storage.blob import BlobServiceClient


def get_azure_connection():
    connect_str = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    return blob_service_client


def download_blob(container_name, blob_name, download_file_path):
    blob_service_client = get_azure_connection()
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())


if __name__ == "__main__":
    # Example usage
    container_name = "your-container-name"
    blob_name = "sample_medical_data.csv"
    download_file_path = "../data/sample_medical_data.csv"
    download_blob(container_name, blob_name, download_file_path)
