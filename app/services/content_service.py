import os
from app.services.storage import load_local_file


class ContentService:
    def __init__(self):
        self.local_content_path = "content"
        self.files = {
            "events": "events.json",
            "news": "news.yaml",
            "faq": "faq.json",
        }

    def get_content(self, content_type: str):
        filename = self.files.get(content_type)
        if not filename:
            raise ValueError(f"Unknown content type: {content_type}")

        file_path = os.path.join(self.local_content_path, filename)
        return load_local_file(file_path)


content_service = ContentService()