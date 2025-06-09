from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv

load_dotenv()

uri = os.environ.get("MONGODB_URI")
if not uri:
    raise ValueError("MONGODB_URI environment variable is not set.")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged the deployment. You successfully connected to MongoDB! :)")
except Exception as e:
    print(f"An error occurred: {e}")