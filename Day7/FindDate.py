#yyyy-mm-dd all dates
#example:'I have work on 2024-02-02 and 2024-11-02'
import re

def words_fn(inp_str):
    pattern=r'\b\d{4}[/-]\d{2}[/-]\d{2}\w*'
    matches=re.findall(pattern,inp_str,re.IGNORECASE)
    return matches

# print("Enter an input string:")
# inpt_str=input()
inpt_str='I have work on 2024-02-02 and 2024/11/02'
matches=words_fn(inpt_str)
print("Dates in string :")
print(matches)