import os
import django

# Set up Django environment (only needed when running script independently)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="Dede")
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")


# List all books in a specific library
library = Library.objects.get(name="Moi_lib")
books_in_library = library.books.all()
print(f"Books in {library.name} library: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a specific library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")