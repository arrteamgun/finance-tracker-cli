from config import ROOT_DIR
import csv
from utils.utils import readfile, change_file
import datetime


class FileService:
    def __init__(self, root_dir: str = ROOT_DIR) -> None:
        self.root_dir = root_dir

    def add(self, entry: list):
        with open(ROOT_DIR + "/data/operations.csv", "a", encoding="utf8") as writer:
            datawriter = csv.writer(writer, lineterminator="\n")
            datawriter.writerow(entry)

    def search(self, category: str = None, amount: float = None, date: datetime.date = None) -> list:
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

    def update(self, id: int, new_date: datetime.date = None, new_amount: float = None, new_description: str = None):
        lines = readfile()
        result = (new_date,  new_description, new_amount)
        for ind, l in enumerate(lines):
            parts = l.strip().split(',')
            l_args = (parts[1], parts[2], parts[3])
            if int(parts[0]) == id:
                result = [x[1] or x[0] for x in  zip(l_args, result)]
                result.insert(0,parts[0])
                cat = ""
                if float(result[-1]) > 0:
                    cat = "Доход"
                else:
                    cat = "Расход"
                result.insert(4, cat)
                result = list(map(str, result))
                change_file(line=result, index=ind+1)