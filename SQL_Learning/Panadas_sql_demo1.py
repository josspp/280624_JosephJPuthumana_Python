import sqlite3
import pandas as pd

connection = sqlite3.connect(r"D:\Training\280624_JosephJPuthumana_Python\SQL_Learning\Chinook_Sqlite.sqlite")
curr=connection.cursor()
#curr.execute("SELECT name FROM sqlite_master WHERE type='table';")

#tables=curr.fetchall()
#query="""
#SELECT * FROM Customer limit 20
#"""
#df_customers=pd.read_sql_query(query,connection)
#print(df_customers)
#connection.close()

#Determine the total sales for each country in the invoice tabel.
#query="""
#SELECT BillingCountry, SUM(Total) as TotalSales
#FROM Invoice
#GROUP BY BillingCountry
#"""
#df_customers=pd.read_sql_query(query,connection)
#print(df_customers)
#connection.close()

#query="""
#SELECT *
#FROM Invoice
#"""
#df_customers=pd.read_sql_query(query,connection)
#pandas code here
#df_customers.groupby("BillingCountry")['Total'].sum().reset_index()

#print(df_customers)



#connection.close()
