class SearchService:
    def search_book(self, book):
        print(f"Searching for book: {book}")


class Library:
    def search(self, book):
        service = SearchService()
        service.search_book(book)


library = Library()
library.search("Python Programming")