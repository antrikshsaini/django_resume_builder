from pymongo import MongoClient

try:
    # Replace <username> and <password> with your actual username and password
    client = MongoClient("mongodb+srv://antrikshsaini96:a0CTNOASjqJzLf4T@clusterproject.4zbso.mongodb.net/?retryWrites=true&w=majority&appName=ClusterProject")
    db = client['ClusterProject']  # Use the database name

    if db is not None:
        print("Database is connected successfully")
    else:
        print("Failed to connect to the database")
except Exception as e:
    print("Error connecting to MongoDB:", e)
