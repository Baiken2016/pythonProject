import pandas as pd

import pandas.core.frame
import csv
ages = []
sexs = []
bmis = []
children = []
smoker = []
region = []
charges = []
def data_collector(lst_name, file_name, column_name):
    with open (file_name) as csv_info:
        csv_info_reader = csv.DictReader(csv_info)
        for row in csv_info_reader:
            lst_name.append(row[column_name])
    return lst_name
data_collector(ages, 'insurance.csv', 'age')
data_collector(sexs, 'insurance.csv', 'sex')
data_collector(bmis, 'insurance.csv', 'bmi')
data_collector(children, 'insurance.csv', 'children')
data_collector(smoker, 'insurance.csv', 'smoker')
data_collector(region, 'insurance.csv', 'region')
data_collector(charges, 'insurance.csv', 'charges')
class PatientsInfo:
    def __init__(self, patients_ages, patients_sexs, patients_region, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexs = patients_sexs
        self.patients_region = patients_region
        self.patients_charges = patients_charges
    def __repr__(self):
        return 'This object helps to analyze info about patients'

    def analyze_age(self):
        total = 0
        for age in self.patients_ages:
            total += int(age)
        return f"The average age is {round(total/len(self.patients_ages), 0)} years."
    def analyze_sexs(self):
        male = 0
        female = 0
        for sex in self.patients_sexs:
            if sex == 'male':
                male +=1
            else:
                female +=1
        return f'The number of male patients is {male}, and number for female patients is {female}'
    def analyze_region(self):
        regions = {}
        for region in self.patients_region:
            if region not in regions:
                regions[region] = 1
            else:
                regions[region] +=1
        return regions
    def analyze_charges(self):
        total = 0
        for charge in self.patients_charges:
            total += float(charge)
        return f'The average charge is {round(total/len(self.patients_charges), 2)} dollars.'

# df = pd.read_csv('insurance.csv')
# print(df)
patients_info = PatientsInfo(ages, sexs, region,charges)
print(patients_info.analyze_charges())