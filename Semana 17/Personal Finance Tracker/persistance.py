import csv

def import_csv_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    student_list = []
    for row in reader:
      student_list.append(row)
    return student_list


def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    writer.writerows(data)