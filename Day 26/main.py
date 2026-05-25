import random
import  pandas
numbers = [1, 2, 3]
new_list = []
for item in numbers:
    new_num = item + 1
    new_list.append(new_num)

print(new_list)

#List Comprehension
new_list_numbers = [n + 2 for n in numbers]
print(new_list_numbers)

"""
PyDev console: starting.
Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
numbers = [1, 2, 3]
new_num = [n*2 for n in numbers]
print(new_num)
[2, 4, 6]
name = "Aman"
letters_list = [letter for letter in name]
print(letters_list)
['A', 'm', 'a', 'n']
new_range_list = [num*2 for num in rang(1, 5)]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'rang' is not defined. Did you mean: 'range'?
new_range_list = [num*2 for num in range(1, 5)]
print(new_range_list)
[2, 4, 6, 8]
"""

#Conditional List Comprehension

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [n.upper() for n in names if len(n) > 5]
print(short_names)
print(long_names)

#Data Overlap Coding Challenge using List Comprehension

with open("./file1.txt") as data_file1:
    data_1 = data_file1.readlines()
file1 =  [int(l.strip()) for l in data_1]
print(file1)

with open("./file2.txt") as data_file2:
    data_2 = data_file2.readlines()
file2 =  [int(l.strip()) for l in data_2]
print(file2)

result = [n for n in file1 if n in file2]
print(result)



# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# student_score = {
#     "Alex": 89,
#     "Beth": 90,
# }

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


#Dictionary Comprehension-1
sentence = "what is the Airspeed Velocity of an Unladen Swallow?"

ch = ""
word_list = []
for letter in sentence:
    if letter !=" ":
        ch = ch+letter
    else:
        # print(ch)
        word_list.append(ch)
        # print(word_list)
        ch = ""
word_list.append(ch)
print(word_list)

result = {word:len(word) for word in word_list}
print(result)


#Dictionary Comprehension-2
weather_c ={
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {days:(temp_c * 9/5)+32 for (days, temp_c) in weather_c.items() }
print(weather_f)


#How to iterate using pandas and Dataframe

student_dict = {
    "student": ["Aman", "Naman", "Priyanka", "Rajani"],
    "score": [56, 76, 98, 85]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through the data frame
#Loop through the rows of data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    print(row.score)