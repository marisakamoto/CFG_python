# Writing a CSV
import csv

field_names = ['name', 'age']


with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames = field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# Writing a CSV

with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))
