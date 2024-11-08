import pandas as pd

student_dictionary={
    "Sangeeth":40,
    "Sam":55,
    "Joseph":65,
    "Gokul":25
}

students=pd.Series(student_dictionary)

print(students)
print("-----------------------------------")
print(students.iloc[0])
print(students.loc['Sam'])
print("-----------------------------------")
print(students[students>50])