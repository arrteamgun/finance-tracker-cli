from abc import ABC, abstractmethod
from datetime import date
from models.ExpenseRecord import ExpenseRecord
from config import ROOT_DIR, DATA_DIR, BALANCE_DIR
from utils.utils import readfile, change_file
import datetime
import csv


class Repository(ABC):

    @abstractmethod
    def add(self, entry: ExpenseRecord) -> None:
        # self.file_service.add(entry)
        pass

    @abstractmethod
    def search(self, category: str = None, amount: float = None, date: date = None) -> ExpenseRecord:
        pass

    def update(self, id: int, new_date: date = None, new_amount: float = None, new_description: str = None) -> None:
        # self.file_service.update(id, new_date, new_amount, new_description)
        pass


class BalanceRepository(Repository):
    def __init__(self):
        pass

    def add(self, sum: float) -> None:
        total = self.search()
        with open(BALANCE_DIR, "w", encoding="utf8") as writer:
            writer.write(str(total))

    def search(self) -> float:
        lines = readfile(path=BALANCE_DIR, header_included=True)
        return float(lines[0])


class OperationsRepository(Repository):
    def __init__(self):
        pass

    def add(self, expense_record: ExpenseRecord) -> None:
        result = [
            expense_record.id,
            expense_record.date,
            expense_record.expense_description,
            expense_record.expense_amount,
            expense_record.category
        ]
        with open(DATA_DIR, "a", encoding="utf8") as writer:
            datawriter = csv.writer(writer, lineterminator="\n")
            datawriter.writerow(result)

    def search(self, category: str = None, amount: float = None, date: date = None) -> list[ExpenseRecord]:
        lines = readfile(path=DATA_DIR)
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
                expence_record = ExpenseRecord(expense_amount=float(
                    parts[3]), expense_description=parts[2])
                expence_record.id = parts[0]
                formatted_date = datetime.datetime.strptime(
                    parts[1], "%Y-%m-%d").date()
                expence_record.date = formatted_date
                expence_record.category = parts[4]
                results.append(expence_record)
        return results

    def update(self, id: int, new_date: datetime.date = None, new_amount: float = None, new_description: str = None) -> ExpenseRecord:
        lines = readfile()
        result = (new_date,  new_description, new_amount)
        for ind, l in enumerate(lines):
            parts = l.strip().split(',')
            l_args = (parts[1], parts[2], parts[3])
            if int(parts[0]) == id:
                result = [x[1] or x[0] for x in zip(l_args, result)]
                result.insert(0, parts[0])
                cat = ""
                if float(result[-1]) > 0:
                    cat = "Доход"
                else:
                    cat = "Расход"
                result.insert(4, cat)
                result = list(map(str, result))
                change_file(DATA_DIR, line=result, index=ind+1)
                return result
                # return expense record to show that line changed
