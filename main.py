from app.trends import get_trends
from app.google_book_api import GoogleBookAPI

trends = get_trends()
book_api = GoogleBookAPI()

for trend in trends:
    print(f'📚 Books related to {trend}')
    result = book_api.search_books(trend)
    if result["totalItems"] > 0:
        for item in result['items']:
            print(item['volumeInfo']['title'])

