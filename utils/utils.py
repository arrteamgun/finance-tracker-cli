from config import ROOT_DIR
import csv


def is_id_unique(id: int):
    data = readfile()
    res = []
    for line in data:
        if line.startswith("Id: "):
            res.append(id == int(line.split("Id: ")[-1]))
    return not any(res)


def readfile(dest: str = ROOT_DIR + "/data/operations.csv", header_included: bool = False):
    with open(ROOT_DIR + "/data/operations.csv", "r", encoding="utf8") as reader:
        if header_included:
            return reader.readlines()
        else:
            return reader.readlines()[1:]


def change_file(path: str = ROOT_DIR, line: list = [], index: int = None) -> None:
    lines = readfile(header_included=True)
    lines[index] = ",".join(line)
    with open(ROOT_DIR + "/data/operations.csv", "w+", encoding='utf-8') as file:
        file.writelines(lines)
