from config import ROOT_DIR

def is_id_unique(id: int):
    data = readfile()
    res = []
    for line in data:
        if line.startswith("Id: "):
            res.append(id == int(line.split("Id: ")[-1]))
    return not any(res)
    
def readfile(dest: str = ROOT_DIR + "/data/operations.csv"):
    with open(ROOT_DIR + "/data/operations.csv", "r", encoding="utf8") as reader:
        return reader.readlines()[1:]

def writer(path: str = ROOT_DIR):
    pass