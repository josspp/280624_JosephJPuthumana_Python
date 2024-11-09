import pandas as pd

data1={
    "Name":["p","q","r"],
    "Age":["1","2","3"],
    "City":["NYK","BRC","LA"]
}
data2={
    "Name":["Mr.XYZ","b","c"],
    "Age":["4","5","6"],
    "City":["KRL","KRN","ANR"]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df3=pd.concat([df1,df2],ignore_index=1)
print(df3)

#df4=df3.loc[ df3["Name"]=="Mr.XYZ","City" ]="Mumbai"
df3.loc[ df3["Name"] == "Mr.XYZ", "City" ] = "Mumbai"
print(df3)



