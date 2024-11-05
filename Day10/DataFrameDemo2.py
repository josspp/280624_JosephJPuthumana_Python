import pandas as pd
Runs={"TCS":{"Qtr1":2500,"Qtr2":"2000","Qtr3":"3000","Qtr4":"2000"},
"WIPRO":{"Qtr1":2800,"Qtr2":"2400","Qtr3":"3600","Qtr4":"2400"},
"L&T":{"Qtr1":2100,"Qtr2":"5700","Qtr3":"35000","Qtr4":"2100"}
      }
df=pd.DataFrame(Runs)
print(df)
print("-----:\n",df.loc['Qtr3',:])
print("+++:\n",df.loc["Qtr1":"Qtr3",:])
#print(df.loc[:,sum('WIPRO'):])