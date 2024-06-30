from my_modules import csv

def filter_data(data, filter_field, filter_value):
    filtered_data = [row for row in data if row[filter_field].startswith(filter_value)]
    return filtered_data

def main():
    file_path = 'my_modules/bestand.csv' 
    data = csv.read_csv(file_path)
    
    filter_field = 'voornaam' 
    filter_value = 'ja'  
    filtered_data = filter_data(data, filter_field, filter_value)
    
    for row in filtered_data:
        print(row)

if __name__ == "__main__":
    main()
