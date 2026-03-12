import time


class TTLCache:
    def __init__(self, ttl_seconds: int):
        self.ttl_seconds = ttl_seconds
        self._store = {}

    def get(self, key):
        item = self._store.get(key)
        if not item:
            return None

        value, expires_at = item
        if time.time() > expires_at:
            del self._store[key]
            return None

        return value

    def set(self, key, value):
        expires_at = time.time() + self.ttl_seconds
        self._store[key] = (value, expires_at)

    def clear(self):
        self._store.clear()