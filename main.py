from app.trends import get_trends
from app.google_book_api import GoogleBookAPI
from dotenv import load_dotenv
from app.mongo_db import get_database
from datetime import datetime

print("🚀 Starting the process..")

load_dotenv()

today = datetime.now().strftime('%Y%m%d')
daily_trend = {
    '_id': today,
    'trends': []
}

book_api = GoogleBookAPI()

db = get_database()
books_collection = db.get_collection('books')
trends_collection = db.get_collection('trends')

for trend in get_trends():
    print("🔍 Searching books for trend: ", trend)
    result = book_api.search_books(trend)
    books_id = []

    if result["totalItems"] > 0:
        for book in result['items']:
            print("📚 Book found: ", book['volumeInfo']['title'])

            book_id = book['id']
            books_id.append(book_id)
            book['_id'] = book_id
            del book['id']

            existing_book = books_collection.find_one({'_id': book_id})
            if existing_book is None:
                books_collection.insert_one(book)

            books_collection.update_one({'_id': book_id}, {'$addToSet': {'trends': trend}}, upsert=True)

    if len(books_id) > 0:
        daily_trend['trends'].append({
            'name': trend,
            'books': books_id
        })

if trends_collection.find_one({'_id': today}) is None:
    print("💾 Saving trends")
    trends_collection.insert_one(daily_trend)

print("✅ Done")
