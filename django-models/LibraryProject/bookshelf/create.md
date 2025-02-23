# Create a Book Instance in Django Shell

## Command
To create a new book instance with the title **1984** author **George Orwell** and publication_year **1949**, run the following command in the Django shell

```python
# Import the Book model from your app
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Ouput the created book
print(book)

# Expected Output
1948  by George Orwell
```
This confirms that the book instance was successfully created in the database.
```