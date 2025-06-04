class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True


def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre: ")

    book = Book(title, author, genre)
    library.append(book)


def search_book(library):
    title = input("Enter the book title to search: ")
    found = False

    for book in library:
        if book.title.lower() == title.lower():
            print("Book Found:")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Genre: {book.genre}")
            found = True
            break

    if not found:
        print("Book not found in the library.")


def update_book(library):
    title = input("Enter the book title to update: ")
    found = False

    for book in library:
        if book.title.lower() == title.lower():
            print("Enter the updated details:")
            author = input("Enter the author's name: ")
            genre = input("Enter the genre: ")

            book.author = author
            book.genre = genre

            print("Book details updated successfully.")
            found = True
            break

    if not found:
        print("Book not found in the library.")


def remove_book(library):
    title = input("Enter the book title to remove: ")
    found = False

    for book in library:
        if book.title.lower() == title.lower():
            library.remove(book)
            print("Book removed successfully.")
            found = True
            break

    if not found:
        print("Book not found in the library.")


def display_books(library):
    if len(library) == 0:
        print("The library is empty.")
    else:
        print("Books in the library:")
        for book in library:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Genre: {book.genre}")
            print("---------")


def sort_books(library):
    sort_criterion = input("Enter the sort criterion (title/author/genre): ")

    if sort_criterion.lower() == "title":
        library.sort(key=lambda book: book.title.lower())
    elif sort_criterion.lower() == "author":
        library.sort(key=lambda book: book.author.lower())
    elif sort_criterion.lower() == "genre":
        library.sort(key=lambda book: book.genre.lower())
    else:
        print("Invalid sort criterion.")
        return

    print("Books sorted successfully.")


def total_books(library):
    return len(library)


def check_availability(library):
    title = input("Enter the book title to check availability: ")
    found = False

    for book in library:
        if book.title.lower() == title.lower():
            if book.available:
                print("The book is available.")
            else:
                print("The book is currently borrowed.")
            found = True
            break

    if not found:
        print("Book not found in the library.")


def borrow_book(library):
    title = input("Enter the book title to borrow: ")
    found = False

    for book in library:
        if book.title.lower() == title.lower():
            if book.available:
                book.available = False
                print("Book borrowed successfully.")
            else:
                print("Sorry, the book is currently borrowed.")
            found = True
            break

    if not found:
        print("Book not found in the library.")


def return_book(library):
    title = input("Enter the book title to return: ")
    found = False

    for book in library:
        if book.title.lower() == title.lower():
            if not book.available:
                book.available = True
                print("Book returned successfully.")
            else:
                print("The book is already available in the library.")
            found = True
            break

    if not found:
        print("Book not found in the library.")


# Example usage of the program
library = []

add_book(library)
add_book(library)

display_books(library)

search_book(library)

