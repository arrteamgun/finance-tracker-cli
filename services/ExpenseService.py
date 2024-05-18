from models.ExpenseRecord import ExpenseRecord
from config import ROOT_DIR
import random
from datetime import date
from utils.utils import is_id_unique, readfile
from repository import Repository


class ExpenseService:
    def __init__(self, repo: Repository):
        self.repo = repo

    def save(self, expense_record: ExpenseRecord):
        is_profit = expense_record.expense_amount >= 0
        category_dict = {0: "Расход", 1: "Доход"}
        expense_record.category = category_dict[is_profit]

        rand_id = random.randint(0, 500000)
        while not is_id_unique(rand_id):
            rand_id = random.randint(0, 500000)
        expense_record.id = rand_id
        result = [
            expense_record.id,
            expense_record.date,
            expense_record.expense_description,
            expense_record.expense_amount,
            expense_record.category
        ]
        self.repo.add(result)

    def find(id: int):
        data = readfile()
        res = []
        for line in data:
            if line.startswith("Id: "):
                res.append(id == int(line.split("Id: ")[-1]))
        return not any(res)

    def search(self, category: str = None, amount: float = None, date: date = None):
        return self.repo.search(category, amount, date)

    def update(self, id: int, new_date: date = None, new_amount: float = None, new_description: str = None) -> None:
        self.repo.update(id, new_date, new_amount, new_description)