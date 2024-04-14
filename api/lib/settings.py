import os
import pickle
from threading import Lock


class SettingsDefault:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            with self._lock:
                if not hasattr(self, '_initialized'):
                    self._initialized = True
                    self.excelFolderPath = ""
                    self.databaseURL = "mongodb://localhost:27017/"
                    self.databaseName = "myapp"
                    self._file_path = "./settings.pickle"
                    self._load_settings()

    def _load_settings(self):
        if os.path.exists(self._file_path) and os.path.getsize(self._file_path) > 0:
            with open(self._file_path, "rb") as file:
                data = pickle.load(file)
                self.excelFolderPath = data.get("excelFolderPath", "")
                self.databaseURL = data.get("databaseURL", "mongodb://localhost:27017/")
                self.databaseName = data.get("databaseName", "myapp")

    def save_settings(self):
        with self._lock:
            with open(self._file_path, "wb") as file:
                pickle.dump({
                    "excelFolderPath": self.excelFolderPath,
                    "databaseURL": self.databaseURL,
                    "databaseName": self.databaseName
                }, file)
        self._load_settings()


settings = SettingsDefault()
