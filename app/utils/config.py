import os


class Config:
    APP_NAME = os.getenv("APP_NAME", "cloud-static-platform")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
    CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "60"))

    STORAGE_MODE = os.getenv("STORAGE_MODE", "local")
    LOCAL_CONTENT_PATH = os.getenv("LOCAL_CONTENT_PATH", "content")

    BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "static-content")
    EVENTS_BLOB_NAME = os.getenv("EVENTS_BLOB_NAME", "events.json")
    NEWS_BLOB_NAME = os.getenv("NEWS_BLOB_NAME", "news.yaml")
    FAQ_BLOB_NAME = os.getenv("FAQ_BLOB_NAME", "faq.json")

    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")