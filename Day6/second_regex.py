import re

def numbers_in_string(string_input):
    """pattern=r'\bs\w*'"""
    pattern=r'\bs\w+'
    Result=re.findall(pattern,test_string,re.IGNORECASE)
    if Result:
        print("success")
        return Result
    else:
        print("unsuccess")
        
test_string='my son is 20 years and 10 days sold S8 phone'

numbers_in_string(test_string)
