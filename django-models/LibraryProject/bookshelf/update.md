# Update a Book Instance in Django Shell

## Command
To update the title of the book **1984** to **Nineteen Eighty-Four**, run the following command in the Django shell

```python
# Import the Book model from your app
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the tile
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated book instance
print(book)

# Expected Output
Nineteen Eighty-Four by George Orwell
```
This confirms that the book instance has been sucessfully updated in the database
```