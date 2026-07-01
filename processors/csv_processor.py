import csv

from processors.type_assessor import detect_type


def open_csv_file(path: str) -> dict:
    columns = {}

    with open(path, 'r') as f:
        sample = f.read(4096)
        dialect = csv.Sniffer().sniff(sample)

        f.seek(0)

        reader = csv.DictReader(f, dialect=dialect)

        for col_name in reader.fieldnames:
            columns[col_name] = []

        for line in reader:
            for col_name in reader.fieldnames:
                columns[col_name].append(line[col_name])

    return columns


def get_columns_types(columns: dict) -> list:
    types = []
    for col_name in columns:
        for i in range(0, len(columns[col_name])):
            types.append(f"{col_name}&&{detect_type(columns[col_name][i])}")
    return types


