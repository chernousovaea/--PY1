import json

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    with open(INPUT_FILE) as f:
        lines = [line for line in json.DictReader(f)]  # TODO реализовать конвертер из csv в json

    with open(INPUT_FILE, "w") as f:
        json.dump(lines, f, indent=4)
        f.write()


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
