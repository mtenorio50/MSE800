# Manage a small library of books - add and show books
class Book:  # Book class to represent a book in the library
    def __init__(self, title, author):  # Constructor to initialize the book's attributes
        self.title = title  # Title of the book
        self.author = author  # Author of the book

    def add_book(library):  # function to add a book to the library
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        # create a new book object with the provided title and author
        book = Book(title, author)
        library.append(book)  # add the book to the library list

    def search_book(library):  # function to search for a book in the library
        title = input("Enter book title to search: ")
        found = False  # flag to check if the book is found
        for book in library:  # iterate through the library list
            # check if the book title matches the search title (case insensitive)
            if book.title.lower() == title.lower():
                print(f"Book found: {book.title} by {book.author}")
                found = True
                break
        if not found:
            # message if the book is not found
            print("No book found with that title.")


library = []  # list to store the books in the library

Book.add_book(library)  # call the add_book function to add a book
Book.add_book(library)  # call the add_book function to add a book

Book.search_book(library)  # call the search_book function to search for a book
