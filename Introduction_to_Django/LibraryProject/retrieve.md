# Retrieve a Book Instance in Django Shell

## Command
To retrieve book instance with the title **1984** from the database, run the following command in the Django shell

```python
# Import the Book model from your app
from bookshelf.models import Book

# Retrieve the book instance with it's attribute eg. title
book = Book.objects.get(title="1984")

# Ouput the created book
print(book)

# Expected Output
1948  by George Orwell
```
This confirms that the book instance is successfully stored and retrieved.
```