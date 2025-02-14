# Delete a Book Instance in Django Shell

## Command
To deletethe book **1984** from the database, run the following command in the Django shell

```python
# Import the Book model from your app
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the tile
book.delete()

# Display the updated book instance
print(book)

# Expected Output
(1, {'library.Book': 1})
```
This confirms that the book instance was successfully deleted from the database.