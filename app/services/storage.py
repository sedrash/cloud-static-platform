import json
import yaml
from azure.storage.blob import BlobServiceClient


def load_local_file(file_path: str):
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    if file_path.endswith(".yaml") or file_path.endswith(".yml"):
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    raise ValueError(f"Unsupported file format: {file_path}")


def load_blob_file(connection_string: str, container_name: str, blob_name: str):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    content = blob_client.download_blob().readall().decode("utf-8")

    if blob_name.endswith(".json"):
        return json.loads(content)

    if blob_name.endswith(".yaml") or blob_name.endswith(".yml"):
        return yaml.safe_load(content)

    raise ValueError(f"Unsupported blob format: {blob_name}")