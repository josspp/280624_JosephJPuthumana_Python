import re

def numbers_in_string(string_input):
    pattern='\d+'
    Result=re.findall(pattern,test_string)
    if Result:
        print("success")
        return Result
    else:
        print("unsuccess")
        
test_string='i am 20 years and 10 days old'

numbers_in_string(test_string)
