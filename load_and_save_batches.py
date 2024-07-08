import csv
import uuid

def load_batches_from_csv(file_path):
    batches = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['count'] = int(row['count'])
                row['software_version'] = float(row['software_version'])
                batches.append(row)
    except FileNotFoundError:
        print(f"File {file_path} not found. Starting with an empty list.")
    return batches

def save_batches_to_csv(file_path, batches):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["unique_id", "name", "count", "special_ability", "software_version"])
        writer.writeheader()
        writer.writerows(batches)