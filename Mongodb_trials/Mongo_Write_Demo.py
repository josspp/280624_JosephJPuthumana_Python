from pymongo import MongoClient
import pandas as pd

connection_string= r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client= MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("Connected to Atlas")

    db= client['ust_live_quiz']

    collection = db['basic_collection_test']

    sample_data= {
        "name":"Sangeeth",
        "age":27,
        "city":"Kerala",
        "Skill":"Programmmig"
    }
#    results = collection.find().limit(5)
    collection.insert_one(sample_data)
    print("Insert success")

    #for doc in results:
    #    print(doc)
    #    break
except Exception as e:
    print(e)

#result_list= list(results)
#print(type(result_list))
#print(result_list[:4])


#df=pd.DataFrame(result_list)
#print(df.head())
#print(df.columns)
