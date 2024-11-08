#find words starting with specifica letter; let that be s
import re

def StringStartWith(inputString):
    pattern=r'\bs\w*'
    matches=re.findall(pattern,inputString,re.IGNORECASE)
    return matches

print("Enter an input string:")
inputString=input()
matches=StringStartWith(inputString)
print("Words starting with s :")
print(matches)