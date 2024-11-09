import pandas as pd

data1={
    "Name":["RRR","ABC","XYZ","Joseph"],
    "Age":["19","22","18","29"],
    "Birth City":["Banglore","Chennai","Hyderabad","Ernakulam"],
    #"Work Experience":["2.0","1.0","3.0"]
}
data2={
    "Name":["RRR","ABC","XYZ"],
    #"Age":["1","2","3"],
    "Work City":["NYC","BRK","LA"],
    "Work Experience":["1.0","2.0","3.0"]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

df3=pd.merge(df1,df2,on="Name",how="outer")
#print(df3)

df3.loc[ df3["Name"]=="Joseph","Work Experience" ]= df3["Work Experience"].astype(float).mean()
print(df3)

df3.to_csv("test_output.csv",index=False)


