import argparse
from models.ExpenseRecord import ExpenseRecord
from services.ExpenseService import ExpenseService
from services.FileService import FileService
from repository import Repository
from datetime import date


def get_console_print(data: list):
    header = ["id", "date", "description", "amount", "category"]
    print(*header, sep="\t")
    if data:
        for row in data:
            print(*row, sep="\t")


def app(service: ExpenseService):
    parser = argparse.ArgumentParser(
        description="Adding expenses to record-file")
    subparser = parser.add_subparsers(dest="command")

    # add
    parser_add = subparser.add_parser("add", help="Add an expense record")
    parser_add.add_argument("amount")
    parser_add.add_argument("description")

    # search
    parser_search = subparser.add_parser(
        "search", help="Find records by given filter")
    parser_search.add_argument("-a", "--amount", help="Expense amount",
                               type=float, default=None)
    parser_search.add_argument("-d", "--date", help="date of operation")
    parser_search.add_argument("-c", "--category", help="category")

    # update
    parser_update = subparser.add_parser(
        "update", help="Change an attribute in found by given ID record")
    parser_update.add_argument(
        "id", help="Record's id. Use 'search' command to discover id", type=int)
    parser_update.add_argument("-a", "--amount", help="Expense amount",
                               type=float, default=None)
    parser_update.add_argument("-d", "--date", help="date of operation")
    parser_update.add_argument("-ds", "--description", help="description")

    args = parser.parse_args()

    if args.command == 'add':
        record = ExpenseRecord(float(args.amount), args.description)
        service.save(record)
    elif args.command == 'search':
        if args.date:
            y, m, d = map(int, args.date.split('-'))
            search_date = date(y, m, d)
            get_console_print(service.search(
                amount=args.amount, category=args.category, date=search_date))
        else:
            get_console_print(service.search(
                amount=args.amount, category=args.category))
    elif args.command == 'update':
        if args.date:
            y, m, d = map(int, args.date.split('-'))
            search_date = date(y, m, d)
            service.update(args.id, new_amount=args.amount,
                           new_description=args.description, new_date=search_date)
        else:
            service.update(args.id, new_amount=args.amount,
                           new_description=args.description)


file_service = FileService()
repo = Repository(file_service)
expense_service = ExpenseService(repo)
app(expense_service)
