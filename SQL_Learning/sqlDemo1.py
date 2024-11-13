import sqlite3

connection = sqlite3.connect(r"D:\Training\280624_JosephJPuthumana_Python\SQL_Learning\Chinook_Sqlite.sqlite")
curr=connection.cursor()

print(curr)

curr.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables=curr.fetchall()
for table in tables:
    print(table)

print("Finished")




