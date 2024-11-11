import pandas as pd

df=pd.read_csv(r"D:\Training\280624_JosephJPuthumana_Python\Titanic\titanic.csv")

#compare the avg age of passengers survived with those didn't

# Group by "Survived" and calculate the mean of the "Age" column
age_comparison = df.groupby('Survived')['Age'].mean()

# Print the result
print("Age comparison:\n",age_comparison)

#2 Calculate the survival rate by gender
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()


print("Survival rate by gender:\n",survival_rate_by_gender)

df["Family Size"]=df["SibSp"]+df["Pclass"]

#print(df[['Name',"SibSp","Pclass","Family Size"]].head())

family_survival_rate = df.groupby('Family Size')['Survived'].mean().reset_index()
family_survival_rate.rename(columns={'Survived': 'Family Survival Rate'}, inplace=True)

df = pd.merge(df, family_survival_rate, on='Family Size', how='left')

# Step 4: Display the resulting DataFrame
print(df[['Name', 'Family Size', 'Survived', 'Family Survival Rate']].head())