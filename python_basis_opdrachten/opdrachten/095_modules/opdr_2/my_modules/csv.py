import csv

def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def filter(data, filterveld, filterwaarde):
    filtered_data = [row for row in data if row[filterveld].startswith(filterwaarde)]
    return filtered_data
