# opdr_1.py
import os
import my_modules.csv as csv_module

def main():
    file_path = 'data.csv'  # Verander de naam van het CSV-bestand naar wat je wilt testen
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} bestaat niet.")
        return
    
    data = csv_module.read_csv(file_path)
    print(data)

if __name__ == "__main__":
    main()
