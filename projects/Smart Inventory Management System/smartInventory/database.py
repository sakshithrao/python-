import json


def read_data(file_path):

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def write_data(file_path, data):

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)