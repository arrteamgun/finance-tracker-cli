import datetime


class ExpenseRecord:
    def __init__(self, expense_amount: float, expense_description: str) -> None:
        self.date = datetime.date.today()
        self.expense_amount = expense_amount
        self.expense_description = expense_description
        self.category = ""
        self.id = 0
