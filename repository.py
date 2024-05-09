from services.FileService import FileService
from datetime import date

class Repository:
    def __init__(self, fs: FileService):
        self.file_service = fs

    def add(self, entry: list):
        self.file_service.add(entry)

    def search(self, category: str = None, amount: float = None, date: date = None):
        return self.file_service.search(category, amount, date)