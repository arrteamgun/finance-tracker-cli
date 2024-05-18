from services.FileService import FileService
from datetime import date


class Repository:
    def __init__(self, fs: FileService):
        self.file_service = fs

    def add(self, entry: list) -> None:
        self.file_service.add(entry)

    def search(self, category: str = None, amount: float = None, date: date = None) -> list:
        return self.file_service.search(category, amount, date)

    def update(self, id: int, new_date: date = None, new_amount: float = None, new_description: str = None) -> None:
        self.file_service.update(id, new_date, new_amount, new_description)
