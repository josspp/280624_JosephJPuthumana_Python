import pandas as pd

df=pd.read_csv(r"D:\Training\280624_JosephJPuthumana_Python\Titanic\titanic.csv")
#print(df.head())
df1=df.loc[:,"Age"].head(5)
#print(df1)
df2=df[['Age','Sex']].head()
#print(df2)
df3=df[df["Age"]<25]
ageAbove25=len(df3.index)
#print(df3)
#print(r"AgeAbove25:",ageAbove25)
AgeMean=df["Age"].mean()

#print("Age Mean:",AgeMean)

#df5=df[df["Age"]<25]
#df6=df[df5["Sex"]="male"]

#print(df6)
#df_male=df[df["Sex"]=="male"]
#print(df_male)
#df_age=df_male[df_male["Age"]<25]
#df7=df_age["Fare"].mean()
#print(df7)
df_final=df[ (df["Sex"]=="male") & (df["Age"]<25) ]
#print(df_final)
#df_final.to_csv("Filtered_Data.csv",index=False)


df_Survived=len(df["Survived"]=="1")

total_pass=len(df.index)
print(total_pass)
perSurviced=((df_Survived)\(total_pass))*100
print(perSurviced)
