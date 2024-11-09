import pandas as pd

data={
    "Store":["Store1","Store1","Store2","Store2","Store3","Store3","Store4","Store5"],
    "Region":["North","North","South","South","East","East","North","South"],
    "Sales":["200","150","300","250","400","350","100","200"]
}

df=pd.DataFrame(data)

print(df)
df["Sales"] = pd.to_numeric(df["Sales"])

# Group by "Store" and sum the "Sales"
grouped_sales = df.groupby("Store")["Sales"].sum()
grouped_region = df.groupby("Region")["Sales"].sum()
# Print the result
#print(grouped_sales)
print(grouped_region)

merged_df_l=pd.merge(df,grouped_region,on="Region",how="left",suffixes=("_Store","_Region"))
merged_df_r=pd.merge(df,grouped_region,on="Region",how="right",suffixes=("_Store","_Region"))
merged_df_i=pd.merge(df,grouped_region,on="Region",how="inner",suffixes=("_Store","_Region"))
merged_df_o=pd.merge(df,grouped_region,on="Region",how="outer",suffixes=("_Store","_Region"))

print("LEFT JOIN\n",merged_df_l)
print("RIGHT JOIN\n",merged_df_r)
print("INNER JOIN\n",merged_df_i)
print("OUTER JOIN\n",merged_df_o)
print("In conclusion left=inner\nright=outer")