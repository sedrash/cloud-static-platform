import json
import yaml


def load_local_file(file_path: str):
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    if file_path.endswith(".yaml") or file_path.endswith(".yml"):
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    raise ValueError(f"Unsupported file format: {file_path}")