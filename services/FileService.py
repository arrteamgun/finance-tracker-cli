from config import ROOT_DIR
import csv
from utils.utils import readfile
import datetime


class FileService:
    def __init__(self, root_dir: str = ROOT_DIR) -> None:
        self.root_dir = root_dir

    def add(self, entry: list):
        with open(ROOT_DIR + "/data/operations.csv", "a", encoding="utf8") as writer:
            datawriter = csv.writer(writer, lineterminator="\n")
            datawriter.writerow(entry)

    def search(self, category: str = None, amount: float = None, date: datetime.date = None):
        lines = readfile()
        results = []
        for line in lines:
            parts = line.strip().split(',')
            if category and parts and parts[-1] == category:
                if parts[-1] == category:
                    pass
                else:
                    parts = []
            if amount is not None and parts:
                if float(parts[3]) == amount:
                    pass
                else:
                    parts = []
            if date and parts:
                formatted_date = datetime.datetime.strptime(
                    parts[1], "%Y-%m-%d").date()
                if formatted_date == date:
                    pass
                else:
                    parts = []
            if parts:
                results.append(parts)
        return results
