from typing import Dict, Union, List, Optional
from collections import defaultdict

class LibraryManager:
    def __init__(self):
        # Initialize an empty dictionary to store book information
        self.books: Dict[str, Dict[str, Union[str, int]]] = {}
    
    def add_book(self, isbn: str, title: str, author: str, publisher: str, volume: str, year: int) -> None:
        """Add a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year
            }
            print(f"Book '{title}' added to the library.")

    def remove_book(self, isbn: str) -> None:
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} has been removed.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def get_book(self, isbn: str) -> Optional[Dict[str, Union[str, int]]]:
        """Retrieve and display the details of a book using its ISBN."""
        return self.books.get(isbn, None)
    
    def search_books(self, title: Optional[str] = None, author: Optional[str] = None) -> List[Dict[str, Union[str, int]]]:
        """Search for books by title or author."""
        results = []
        for book in self.books.values():
            if (title and title.lower() in book['title'].lower()) or (author and author.lower() in book['author'].lower()):
                results.append(book)
        return results
    
    def list_books(self) -> List[Dict[str, Union[str, int]]]:
        """List all books currently in the library."""
        return list(self.books.values())
    
    def update_book(self, isbn: str, title: Optional[str] = None, author: Optional[str] = None,
                    publisher: Optional[str] = None, volume: Optional[str] = None, year: Optional[int] = None) -> None:
        """Update the details of an existing book."""
        if isbn in self.books:
            book = self.books[isbn]
            if title:
                book['title'] = title
            if author:
                book['author'] = author
            if publisher:
                book['publisher'] = publisher
            if volume:
                book['volume'] = volume
            if year:
                book['year'] = year
            print(f"Book with ISBN {isbn} has been updated.")
        else:
            print(f"No book found with ISBN {isbn}.")
    
    def is_book_available(self, isbn: str) -> bool:
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books

def display_menu():
    print("\n--- Library Management System Menu ---")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Retrieve book details")
    print("4. Search for books")
    print("5. List all books")
    print("6. Update book details")
    print("7. Check if a book is available")
    print("8. Exit")

def get_book_input(prompt: str) -> Dict[str, Union[str, int]]:
    """Helper function to get book details from user."""
    print(prompt)
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    publisher = input("Enter publisher: ")
    volume = input("Enter volume: ")
    year = int(input("Enter year of publication: "))
    return {
        'isbn': isbn,
        'title': title,
        'author': author,
        'publisher': publisher,
        'volume': volume,
        'year': year
    }

def get_search_input() -> Dict[str, Optional[str]]:
    """Helper function to get search criteria from user."""
    title = input("Enter title to search (or press Enter to skip): ")
    author = input("Enter author to search (or press Enter to skip): ")
    return {
        'title': title if title else None,
        'author': author if author else None
    }

def main():
    library = LibraryManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            book = get_book_input("Enter details for the book to add:")
            library.add_book(book['isbn'], book['title'], book['author'], book['publisher'], book['volume'], book['year'])
        
        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)
        
        elif choice == '3':
            isbn = input("Enter ISBN of the book to retrieve: ")
            book = library.get_book(isbn)
            if book:
                print("Book Details:", book)
            else:
                print("No book found with that ISBN.")
        
        elif choice == '4':
            search_criteria = get_search_input()
            results = library.search_books(title=search_criteria['title'], author=search_criteria['author'])
            if results:
                print("Search Results:")
                for book in results:
                    print(book)
            else:
                print("No books found matching the criteria.")
        
        elif choice == '5':
            all_books = library.list_books()
            if all_books:
                print("All Books in Library:")
                for book in all_books:
                    print(book)
            else:
                print("No books in the library.")
        
        elif choice == '6':
            isbn = input("Enter ISBN of the book to update: ")
            print("Enter new details (leave blank to keep current value):")
            book = get_book_input("Update book details:")
            library.update_book(
                isbn, 
                title=book['title'], 
                author=book['author'], 
                publisher=book['publisher'], 
                volume=book['volume'], 
                year=book['year']
            )
        
        elif choice == '7':
            isbn = input("Enter ISBN to check availability: ")
            is_available = library.is_book_available(isbn)
            print("Book is available." if is_available else "Book is not available.")
        
        elif choice == '8':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
