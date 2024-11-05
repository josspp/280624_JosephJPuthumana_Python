import pandas as pd
"""import numpy as np"""
student_dictionary={
    "RRR":100,
    "Mr. ABC":55,
    "Miss. M":75,
}
students=pd.Series(student_dictionary)
print(students.iloc[2])