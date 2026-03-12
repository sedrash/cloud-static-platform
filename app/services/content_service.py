import os
from app.services.cache import TTLCache
from app.services.storage import load_local_file, load_blob_file
from app.utils.config import Config


cache = TTLCache(Config.CACHE_TTL_SECONDS)


class ContentService:
    def __init__(self):
        self.storage_mode = Config.STORAGE_MODE
        self.local_content_path = Config.LOCAL_CONTENT_PATH
        self.container_name = Config.BLOB_CONTAINER_NAME
        self.connection_string = Config.AZURE_STORAGE_CONNECTION_STRING

        self.files = {
            "events": Config.EVENTS_BLOB_NAME,
            "news": Config.NEWS_BLOB_NAME,
            "faq": Config.FAQ_BLOB_NAME,
        }

    def get_content(self, content_type: str):
        cached = cache.get(content_type)
        if cached is not None:
            return cached

        filename = self.files.get(content_type)
        if not filename:
            raise ValueError(f"Unknown content type: {content_type}")

        if self.storage_mode == "local":
            file_path = os.path.join(self.local_content_path, filename)
            data = load_local_file(file_path)
        elif self.storage_mode == "azure":
            data = load_blob_file(
                self.connection_string,
                self.container_name,
                filename,
            )
        else:
            raise ValueError(f"Unsupported storage mode: {self.storage_mode}")

        cache.set(content_type, data)
        return data


content_service = ContentService()