from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId


connection_string= r"mongodb+srv://rohithrajreganti:rohithrajreganti@cluster0.rd7dn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client= MongoClient(connection_string,tlsAllowInvalidCertificates=True)
    print("Connected to mongo Atlas")

    db= client['ust_live_quiz']

    collection = db['basic_collection_test']

#    sample_data= {
#        "name":"Sangeeth",
#        "age":27,
#        "city":"Kerala",
#        "Skill":"Programmmig"
#    }
#    results = collection.find().limit(5)
    doc_id="673836daa4958cb8cb9b8dc5"
    query={"_id": ObjectId(doc_id)}

    update = {"$set":{"name":"joseph","city":"KOCHI"}}
#    collection.insert_one(sample_data)
#    print("Insert success")
    result=collection.update_one(query,update)
    #for doc in results:
    #    print(doc)
    #    break
    if (result.matched_count > 0):
        print("There was a match, doc has been found")
except Exception as e:
    print(e)