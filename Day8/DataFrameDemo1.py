import pandas as pd
dict_main={"a":['1','3'],"b":["2","5"],"c":["3","6"]}
inp=''
while(inp!='3'):
    print("Please choose one of the below options:\n1.Add to Dictionary\n2.Data frame dispaly\n3.Exit")
    inp=input()
    if(inp=="1"):
        print("Enter key to add:")
        key=input()
        print("Enter value to add :")
        val=input()
        dict_main[key]=val.split(",")
    elif(inp=="2"):
        df=pd.DataFrame(dict_main)
        print(df)