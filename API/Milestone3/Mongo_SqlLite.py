import pymongo
import sqlite3
import pandas as pd
 
def TransferMoviewData(mongo_uri, database_name, collection_name, sqlite_db_path):
    try:
        # Connect to MongoDB
        mongo_client = pymongo.MongoClient(mongo_uri)
        mongo_db = mongo_client[database_name]
        mongo_collection = mongo_db[collection_name]
 
        print("Connected to MongoDB successfully.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return
 
    try:
        # Connect to SQLite
        sqlite_conn = sqlite3.connect(sqlite_db_path)
        sqlite_cursor = sqlite_conn.cursor()
 
        # Create a table in SQLite if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS movies (
            id TEXT PRIMARY KEY,
            title TEXT,
            directors TEXT,
            released INTEGER,
            genres TEXT
        );
        """
        sqlite_cursor.execute(create_table_query)
        sqlite_conn.commit()
 
        print("Connected to SQLite and table created.")
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite: {e}")
        mongo_client.close()
        return
 
    try:
        # Fetch data from MongoDB
        # movies_data = mongo_collection.find()      
        movies_data = ""  
 
        # Insert data into SQLite
        for movie in movies_data:
            # Extract data from MongoDB document
            genres_val="";
            directors_val="";
 
            movie_id = str(movie.get("_id", ""))
            title = movie.get("title", "Unknown")
            directors = movie.get("directors", "Unknown")
            released = movie.get("released", 0)
            genres = movie.get("genres", "Unknown")
 
            for gen in genres :
                if len(genres_val)>0 : genres_val += ", "
                genres_val += gen
 
            for dir in directors : 
                if len(directors_val)>0 : directors_val += ", "
                directors_val += dir
 
            directors = directors_val
            genres = genres_val
 
            # Insert into SQLite
            insert_query = """
            INSERT OR REPLACE INTO movies (id, title, directors, released, genres)
            VALUES (?, ?, ?, ?, ?);
            """
            sqlite_cursor.execute(insert_query, (movie_id, title, directors, released, genres))
        sqlite_conn.commit()
        print("Data transfer completed successfully!")
 
        movies_data = sqlite_cursor.execute("select * from movies limit 100")
        df_data = pd.DataFrame(movies_data)
        print(df_data)
 
    except Exception as e:
        print(f"Error during data transfer: {e}")
    finally:
        # Close connections
        try:
            sqlite_conn.close()
            print("SQLite connection closed.")
        except Exception as e:
            print(f"Error closing SQLite connection: {e}")
 
        try:
            mongo_client.close()
            print("MongoDB connection closed.")
        except Exception as e:
            print(f"Error closing MongoDB connection: {e}")
 
# Configuration
MONGO_URI = "mongodb+srv://josephjputhumana:$Rupee123@cluster0.bjuql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "sample_mflix"
COLLECTION_NAME = "movies"
SQLITE_DB_PATH = "movies.db"
 
# Run the transfer
TransferMoviewData(MONGO_URI, DATABASE_NAME, COLLECTION_NAME, SQLITE_DB_PATH)