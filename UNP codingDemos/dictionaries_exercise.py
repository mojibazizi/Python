#Here's a grade/attendance book for a teacher's students
    ##It contains a dictionary of dictionaries
from typing import Concatenate


Rohib = {
    'name': 'Rohib',
    'grades': [100, 78, 95, 87, 90],
    'attendance': [True, True, True, True, True],
}

Mohib = {
    'name': 'Mohib',
    'grades': [76, 75, 89, 87, 100],
    'attendance': [False, True, True, True, True],

}

Shaima = {
    'name': 'Shaima',
    'grades': [100, 100, 98, 76, 75],
    'attendance': [True, True, True, True, True]
}
     #add each student to a dictionary using a unique student ID
students = {'1': Rohib, '2': Mohib, '3': Shaima}

#get number of students
print(len(students)) #number of keys

#get all of the students IDs (keys) by using the built-in dict keys method
 ##get all the students IDs
print(students.keys())

# You can also get the keys by iterating over a dictionary itself
##iterate over students
for k in students:
    print('keys:', k)

# Get Rohib's attendance
Rohib = students['1']
print(Rohib['attendance'])

# Get Shaima's grade
Shaima = students.get('3')
print(Shaima.get('grades'))

# Use the built-in dict items method to get all key:value pairs for a dictionary
##Get all key:value pairs for Mohib
Mohib = students.get('2')
items = Mohib.items() # returns sequence of tuples
##iterate over student dictionaries
for key, val in items:
    print(key, val)

#Get average student grade for all assignments 
grades = []
items = students.items() #key:value pair's for students
for key, val in items:
    for g in val['grades']:
        grades.append(g)

#Average grade 
print(round(sum(grades)/ len(grades)))

# another way to do this 
grades_concatenated = []
items = students.items()
for key, val in items:
    grades_concatenated += val['grades']

#average grade
print('Your average class is:', round(sum(grades_concatenated) / len(grades_concatenated)))