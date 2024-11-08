def print_results(filename,target_school):
    

    for line in file:
        line=line[:-1]
        listCreated=line.split(",")
        print(listCreated)
        if(listCreated[1].strip() ==target_school.strip()):
            print(line)
            
        print("...")

file=open("D:/Training/259398_PythonTraining/DAY08/sample.csv",'r')
print_results(file,"UST")
print('-----------------------')
file.close