from models.ExpenseRecord import ExpenseRecord
from config import ROOT_DIR
import random
from datetime import date
from utils.utils import is_id_unique, readfile
from services.repository import Repository, BalanceRepository, OperationsRepository


class ExpenseService:
    def __init__(self, repo_operation: OperationsRepository, repo_balance: BalanceRepository):
        self.repo_operation = repo_operation
        self.repo_balance = repo_balance

    def save(self, expense_record: ExpenseRecord):
        is_profit = expense_record.expense_amount >= 0
        category_dict = {0: "Расход", 1: "Доход"}
        expense_record.category = category_dict[is_profit]

        rand_id = random.randint(0, 500000)
        while not is_id_unique(rand_id):
            rand_id = random.randint(0, 500000)
        expense_record.id = rand_id

        self.repo_operation.add(expense_record)
        self.repo_balance.add(expense_record.expense_amount)

    def find(id: int):
        data = readfile()
        res = []
        for line in data:
            if line.startswith("Id: "):
                res.append(id == int(line.split("Id: ")[-1]))
        return not any(res)

    def search(self, category: str = None, amount: float = None, date: date = None) -> list:
        ers = self.repo_operation.search(category, amount, date)
        result = []
        for er in ers:
            row = [er.id, er.date, er.expense_amount,
                   er.expense_description, er.category]
            result.append(row)
        return result
    
    def get_balance(self) -> str:
        return str(self.repo_balance.search())

    def update(self, id: int, new_date: date = None, new_amount: float = None, new_description: str = None) -> list:
        return self.repo_operation.update(id, new_date, new_amount, new_description)
