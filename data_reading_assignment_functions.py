# find the faculty with highest student count who got more than 90%
import csv

def count_students_above_threshold(subject, threshold):
    count = 0
    with open('student_marks.csv', 'r') as file:
        data = csv.DictReader(file)
        for record in data:
            if int(record[subject]) > threshold:
                count += 1
    return count

faculty = {
    'Telugu': 'Amarnath',
    'English': 'Samuel',
    'Maths': 'Murali Krishna',
    'Physics': 'Raja Gopal',
    'Chemistry': 'Ravi',
    'Social': 'Krishna Reddy'
}

highest_student_count = 0
faculty_with_highest_student_count = ''

for subject in faculty.keys():
    student_count = count_students_above_threshold(subject, 90)
    if student_count > highest_student_count:
        highest_student_count = student_count
        faculty_with_highest_student_count = faculty[subject]

if faculty_with_highest_student_count == '':
    print("No faculty has students with scores above 90%.")
else:
    print("Faculty with the highest student count who scored more than 90%:", faculty_with_highest_student_count)

 #  find the faclty with highest pass percentage(>40)
import csv

def calculate_pass_percentage(subject, threshold):
    pass_count = 0
    total_count = 0
    with open('student_marks.csv', 'r') as file:
        data = csv.DictReader(file)
        for record in data:
            if int(record[subject]) > threshold:
                pass_count += 1
            total_count += 1
    pass_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0
    return pass_percentage

faculty = {
    'Telugu': 'Amarnath',
    'English': 'Samuel',
    'Maths': 'Murali Krishna',
    'Physics': 'Raja Gopal',
    'Chemistry': 'Ravi',
    'Social': 'Krishna Reddy'
}

sub_faculty = {}
for subject in faculty.keys():
    pass_percentage = calculate_pass_percentage(subject, 40)
    sub_faculty[subject] = pass_percentage

faculty_with_highest_pass_percentage = max(sub_faculty, key=sub_faculty.get)
pass_percentage = sub_faculty[faculty_with_highest_pass_percentage]

print(f"The faculty with the highest pass percentage (>40%) is {faculty[faculty_with_highest_pass_percentage]} with {pass_percentage}% students who scored more than 40%.")


# find the faculty with least pass percentage(<=40)


import csv

def calculate_pass_percentage(subject, threshold):
    pass_count = 0
    total_count = 0
    with open('student_marks.csv', 'r') as file:
        data = csv.DictReader(file)
        for record in data:
            if int(record[subject]) <= threshold:
                pass_count += 1
            total_count += 1
    pass_percentage = (pass_count / total_count) * 100 if total_count > 0 else 0
    return pass_percentage

faculty = {
    'Telugu': 'Amarnath',
    'English': 'Samuel',
    'Maths': 'Murali Krishna',
    'Physics': 'Raja Gopal',
    'Chemistry': 'Ravi',
    'Social': 'Krishna Reddy'
}

sub_faculty = {}
for subject in faculty.keys():
    pass_percentage = calculate_pass_percentage(subject, 40)
    sub_faculty[subject] = pass_percentage

faculty_with_least_pass_percentage = min(sub_faculty, key=sub_faculty.get)
pass_percentage = sub_faculty[faculty_with_least_pass_percentage]

print(f"The faculty with the least pass percentage (<=40%) is {faculty[faculty_with_least_pass_percentage]} with {pass_percentage}% students who scored less than or equal to 40%.")


# who is the top student with maximum total
import csv

def top_student_max_total(student_marks):
    with open(student_marks, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        total_marks = {}
        for records in data:
            marks = (int(records['Telugu']), int(records['English']), int(records['Maths']), int(records['Physics']), 
                    int(records['Chemistry']), int(records['Social']))
            total = sum(marks)
            total_marks[records['studentname']] = total
        top_student = max(total_marks, key=total_marks.get)
        msg = f"The top student with the maximum total marks is {top_student} with a total of {total_marks[top_student]}"

    return msg

print(top_student_max_total('student_marks.csv'))

# print(f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}")
# who is the best student in maths

import csv

def top_student_max_subject(student_marks, subject):
    with open(student_marks, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        subject_marks = {}
        for records in data:
            marks = int(records[subject])
            subject_marks[records['studentname']] = marks
        students = sorted(subject_marks.items(), key=lambda x: x[1], reverse=True)
        msg = f"The top student in {subject} is {students[0][0]} with a score of {students[0][1]}"

    return msg

print(top_student_max_subject('student_marks.csv', 'Maths'))

 # What is the average mark for each subject, (ignore failures)?
import csv

def avg_mark_sub(student_marks):
    telugu_sum = 0; telugu_count = 0
    english_sum = 0; english_count = 0
    maths_sum = 0; maths_count = 0
    physics_sum = 0; physics_count = 0
    chemistry_sum = 0; chemistry_count = 0
    social_sum = 0; social_count = 0

    pass_mark = 40

    avg_marks = {}

    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for record in data:
            if int(record['Telugu']) >= pass_mark:
                telugu_sum += int(record['Telugu'])
                telugu_count += 1
            if int(record['English']) >= pass_mark:
                english_sum += int(record['English'])
                english_count += 1
            if int(record['Maths']) >= pass_mark:
                maths_sum += int(record['Maths'])
                maths_count += 1
            if int(record['Physics']) >= pass_mark:
                physics_sum += int(record['Physics'])
                physics_count += 1
            if int(record['Chemistry']) >= pass_mark:
                chemistry_sum += int(record['Chemistry'])
                chemistry_count += 1
            if int(record['Social']) >= pass_mark:
                social_sum += int(record['Social'])
                social_count += 1

        avg_marks = {
            'Telugu' : telugu_sum/telugu_count,
            'English' : english_sum/english_count,
            'Mathematics' : maths_sum/maths_count,
            'Physics' : physics_sum/physics_count,
            'Chemistry' : chemistry_sum/chemistry_count,
            'Social' : social_sum/social_count
        }

    Subjects = sorted(avg_marks.items(),key = lambda x: x[1],reverse=True)
    print(Subjects)

    msg6 = (f"Ignoring failures,the Average mark for {Subjects[0][0]} is {round(Subjects[0][1])}",
            f"Ignoring failures,the Average mark for {Subjects[1][0]} is {round(Subjects[1][1])}",
            f"Ignoring failures, the Average mark for {Subjects[2][0]} is {round(Subjects[2][1])}",
            f"Ignoring failures,the Average mark for {Subjects[3][0]} is {round(Subjects[3][1])}",
            f"Ignoring failures, the Average mark for {Subjects[4][0]} is {round(Subjects[4][1])}",
            f"Ignoring failures,the Average mark for {Subjects[5][0]} is {round(Subjects[5][1])}")
    
    return msg6
print(avg_mark_sub('student_marks.csv'))
#  Find the student with least numbers of marks as total.
import csv

def student_least_marks_totla(student_marks):
    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        total_marks = {}
        for records in data:
            marks = (int(records['Telugu']), int(records['English']), int(records['Maths']), int(records['Physics']), 
                    int(records['Chemistry']), int(records['Social']))

            total = sum(marks)
            total_marks[records['studentname']] = total
        students = sorted(total_marks.items(), key=lambda x: x[1])
        msg7 = f"The Student is {students[0][0]} and his Least mark is {students[0][1]}"
    
    return msg7
print(student_least_marks_totla('student_marks.csv'))