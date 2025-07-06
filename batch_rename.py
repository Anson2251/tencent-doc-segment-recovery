import csv
import os

def rename_files(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                original_name = row[0].strip()
                target_name = row[1].strip()
                if os.path.exists(original_name):
                    os.rename(original_name, target_name)
                    print(f"Renamed '{original_name}' to '{target_name}'")
                else:
                    print(f"File '{original_name}' not found, skipping")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python rename_files.py <csv_file>")
    else:
        csv_file = sys.argv[1]
        rename_files(csv_file)