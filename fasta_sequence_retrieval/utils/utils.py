import csv


def read_file(filename):
    data = ""
    with open(filename, "r") as file:
        for line in file:
            data += line
    return data


def save_csv(data, filename):
    with open("output/" + filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def save_text_file(data, filename):
    with open("output/" + filename, "w") as file:
        file.write(data)


def format_text(text):
    formatted_text = []
    for line in text.split("\n"):
        formatted_text.append(" ".join(line.strip().split()))

    return formatted_text


def save_dict_to_csv(fields: list[str], data: dict(), filename: str):
    with open("output/" + filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)
