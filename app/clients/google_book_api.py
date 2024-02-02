import requests

class GoogleBookAPI:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/volumes?orderBy=relevance&printType=BOOKS"

    def search_books(self, search_terms):
        url = f"{self.base_url}&q={search_terms}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}"
