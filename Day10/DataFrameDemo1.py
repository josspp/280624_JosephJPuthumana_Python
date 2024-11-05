"""import pandas as pd
name=pd.Series(["hardi","Virat"])
team=pd.Series(["MI","RCB"])
dic={"Name":name,"Team":team}
df=pd.DataFrame(dic)
print(df)"""

'''import pandas as pd

dictio={
    "Name":["Hardik","Virat"],
    "Team":["1","2"]
}
df=pd.DataFrame(dictio,index=["Rank1","Rank2"])
#print(df)

for row_index, row_value in df.iterrows():
    print("===========")
    print("===========")
    print("Row_index is:\n",row_index)
    print("Row_value is:\n", row_value)'''


import pandas as pd

dictio={
    "Name":["Hardik","Virat"],
    "Team":["1","2"]
}
df=pd.DataFrame(dictio)
print(df)

for col_index, col_value in df.iteritems():
    print("===========")
    print("===========")
    print("Col_index is:\n",col_index)
    print("Col_value is:\n", col_value)
