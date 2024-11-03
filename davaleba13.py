import csv
from statistics import mean

def add_student_info(filepath, student_data):
    records = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        records = list(reader)

    if any(record['id'] == student_data['id'] for record in records):
        print("Student with ID " + student_data['id'] + " already exists.")
        return

    records.append(student_data)
    records.sort(key=lambda x: int(x['id']))

    with open(filepath, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def fetch_students(filepath, student_id=None):
    results = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for entry in reader:
            if student_id is None or entry['id'] == str(student_id):
                results.append(entry)
    
    return results

def average_marks(filepath, subject):
    marks = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for entry in reader:
            if entry['subject_name'] == subject:
                marks.append(float(entry['mark']))

    return mean(marks) if marks else 0

def modify_student_mark(filepath, student_id, subject, updated_mark):
    records = []
    
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        records = list(reader)

    for entry in records:
        if entry['id'] == str(student_id) and entry['subject_name'] == subject:
            entry['mark'] = str(updated_mark)
            break
    else:
        print("Student ID " + str(student_id) + " or subject " + subject + " not found.")
        return

    with open(filepath, mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

file_path = 'students.csv'

new_student = {'id': '6', 'name': 'LEILA', 'age': '20', 'grade': 'B', 'subject_name': 'math', 'mark': '4'}
add_student_info(file_path, new_student)

all_students = fetch_students(file_path)
print("All Students:")
for student in all_students:
    print(student)

specific_student = fetch_students(file_path, student_id=2)
print("Specific Student (ID 2):")
print(specific_student)

subject = 'politics'
average_mark = average_marks(file_path, subject)
print("Average Marks for " + subject + ": " + str(average_mark))

modify_student_mark(file_path, student_id=2, subject='politics', updated_mark=3)
print("Updated Student Records after modifying marks:")
updated_students = fetch_students(file_path)
for student in updated_students:
    print(student)
