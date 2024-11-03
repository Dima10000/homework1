import csv

file_path = 'students.csv'
data = [
    {'id': '1', 'name': 'EKA', 'age': '19', 'grade': 'A', 'subject_name': 'history', 'mark': '3'},
    {'id': '2', 'name': 'MARI', 'age': '19', 'grade': 'B', 'subject_name': 'politics', 'mark': '2'},
    {'id': '3', 'name': 'NINI', 'age': '19', 'grade': 'D', 'subject_name': 'economics', 'mark': '1'},
    {'id': '4', 'name': 'PAATA', 'age': '19', 'grade': 'A', 'subject_name': 'politics', 'mark': '3'},
    {'id': '5', 'name': 'IRAKLI', 'age': '19', 'grade': 'C', 'subject_name': 'law', 'mark': '1'}
]

with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'name', 'age', 'grade', 'subject_name', 'mark'])
    writer.writeheader()
    writer.writerows(data)
