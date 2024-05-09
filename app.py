import argparse
from models.ExpenseRecord import ExpenseRecord
from services.ExpenseService import ExpenseService
from services.FileService import FileService
from repository import Repository
from datetime import date

def get_console_print(data: list):
    for row in data:
        pass

def app(service: ExpenseService):
    parser = argparse.ArgumentParser(
        description="Adding expenses to record-file")
    parser.add_argument("-a", "--amount", help="the exponent",
                        type=float)
    parser.add_argument("-v","--description", help="operation's description",
                        type=str)
    parser.add_argument("-d","--date", help="date of operation")
    parser.add_argument("-b", "--balance")
    args = parser.parse_args()
    record = ExpenseRecord(args.amount, args.description)
    # service.save(record)
    # обрисовать логику
    y = int(args.date.split('-')[0])
    m = int(args.date.split('-')[1])
    d = int(args.date.split('-')[2])
    print(service.search(amount=float(args.amount),
          category="Расход", date=date(y, m, d)))


file_service = FileService()
repo = Repository(file_service)
expense_service = ExpenseService(repo)
app(expense_service)
