import csv

a = []
with open('insurance.csv') as insurance_file:
    insurance_file_reader = csv.DictReader(insurance_file)
    for row in insurance_file_reader:
        a.append(row)
print(a)
