import re

def numbers_in_string(string_input):
    """pattern=r'\bs\w*'"""
    pattern=r'\b\d+[-|\]*\d+[-|\]*d+\w+'
    Result=re.findall(pattern,test_string,re.IGNORECASE)
    if Result:
        print("success")
        return Result
    else:
        print("unsuccess")
        
test_string='i have to take leave on 2024-12-27 and also 2024\12\26'

numbers_in_string(test_string)
