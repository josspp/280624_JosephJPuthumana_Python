import sqlite3

connection = sqlite3.connect(r"D:\Training\280624_JosephJPuthumana_Python\SQL_Learning\Chinook_Sqlite.sqlite")
curr=connection.cursor()

#print(curr)

#curr.execute("SELECT name FROM sqlite_master WHERE type='table';")

#tables=curr.fetchall()
#for table in tables:
#    print(table)

#print("Finished")

#CRUD -> Create, Read, Update, Delete

#Create operations
##CustomerID, FirstNAme, Lastname, Company, Email, Country, Phone
#new_customer=(60,'Rajiv','RR','ABC','Rajiv.rr@gmail.com','IND')
##(CustomerId, FirstName,LastName,Comapany,Email,Country,Phone)
#curr.execute(
#    """
#    INSERT INTO Customer(CustomerId,FirstName,LastName,
#    Company,Email,Country) VALUES (?,?,?,?,?,?)
#    """,new_customer
#)

#connection.commit
#print("New customer added")

#Read that customer that you just wrote to the database



curr.execute("SELECT * FROM Customer WHERE CustomerId=60")
data=curr.fetchall()
for row in data:
    print(row)

desc=curr.description
cols=[col[0] for col in desc]
print(cols)



customer_id=60
new_email='rajiv.rr@ust1.com'

curr.execute(
    """ 
    UPDATE Customer
    SET Email = ?,Company = ?
    WHERE CustomerId = ?
    """,(new_email,'USTInternational',customer_id)
    )

connection.commit()
print("Customer updated")

curr.execute("SELECT * FROM Customer WHERE CustomerId=60")
data=curr.fetchall()
for row in data:
    print(row)

desc=curr.description
cols=[col[0] for col in desc]
print(cols)

#curr.execute("""
#DELETE FRO,
#"""
#)
