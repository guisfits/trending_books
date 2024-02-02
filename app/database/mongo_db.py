from pymongo import MongoClient
import os

def get_database():
    mongodb_url = os.environ.get('MONGODB_URL')

    client = MongoClient(mongodb_url)
    db = client.get_database('trending_books')

    collection_names = db.list_collection_names()

    if not ('books' in collection_names):
        db.create_collection('books')
    
    if not ('trends' in collection_names):
        db.create_collection('trends')

    return db 
