# finance-tracker-cli
It's a simple CRUD-like CLI that helps you to track expense records and store them (with *.csv* format yet)

This project could be useful if you want to implement such activity with similar business logic. It uses *repository pattern* so you can configurate destination type, method or storage as you want.

## Configuration
Simply clone the project. As you run it you could check 
```
python3 app.py -h
```

It has parameters (parsers):
Some basic Git commands are:
```
python3 app.py add - adds a record with sum and description
python3 app.py search - finds record(s) that match parameters you need
python3 app.py update - updates a record parameters by the record's id
python3 app.py balance - shows current balance
```

### Thing to do on the project
+ Justify output for **python3 app.py search**
+ Clean the code, add more abstractions at *ExpenceService.py*
+ Write unit tests for modules