
def print_name_multiple_time():
    name=input("Enter name:")
    """number of times to print name"""
    times=int(input("how many time to print the name:"))

    for repetation in range(times):
        print(str(repetation)+"."+name)
"""Calling the function"""
print_name_multiple_time()