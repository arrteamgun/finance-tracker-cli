from config import ROOT_DIR, DATA_DIR
import csv


def is_id_unique(id: int):
    data = readfile()
    res = []
    for line in data:
        if line.startswith("Id: "):
            res.append(id == int(line.split("Id: ")[-1]))
    return not any(res)


def readfile(path: str = None, header_included: bool = False):
    if not path:
        path = DATA_DIR
    with open(path, "r", encoding="utf8") as reader:
        if header_included:
            return reader.readlines()
        else:
            return reader.readlines()[1:]


def change_file(path: str, line: list = [], index: int = None) -> None:
    lines = readfile(header_included=True)
    lines[index] = ",".join(line) + "\n"
    with open(path, "w+", encoding='utf-8') as file:
        file.writelines(lines)
