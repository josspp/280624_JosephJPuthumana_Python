import sqlite3

connection = sqlite3.connect(r"D:\Training\Chinook_Sqlite.sqlite")
curr=connection.cursor()

print(curr)