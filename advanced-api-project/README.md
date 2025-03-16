# Book API - Django REST Framework

## Overview
This API allows users to perform CRUD (Create, Read, Update, Delete) operations on books. The API uses Django REST Framework (DRF) and provides the following endpoints:

- `GET /api/books/` - List all books
- `GET /api/books/<id>/` - Retrieve a single book
- `POST /api/books/create/` - Create a new book
- `PUT/PATCH /api/books/update/<id>/` - Update an existing book
- `DELETE /api/books/delete/<id>/` - Delete a book

---

## API Endpoints & Views

### 1️⃣ List Books (GET `/api/books/`)
**View:** `BookListView`
- Retrieves a list of all books in the database.
- Uses `ListAPIView` for read-only access.

### 2️⃣ Retrieve a Book (GET `/api/books/<id>/`)
**View:** `BookDetailView`
- Fetches details of a specific book using its `id`.
- Uses `RetrieveAPIView`.

### 3️⃣ Create a Book (POST `/api/books/create/`)
**View:** `BookCreateView`
- Allows adding a new book.
- Expects `title`, `publication_year`, and `author` fields in the request body.

Example request body:
```json
{
    "title": "New Book",
    "publication_year": 2023,
    "author": 2
}
```

### 4️⃣ Update a Book (PUT/PATCH `/api/books/update/<id>/`)
**View:** `BookUpdateView`
- Updates the details of an existing book.
- Accepts both `PUT` (full update) and `PATCH` (partial update) methods.

Example request body for a partial update:
```json
{
    "title": "Updated Book Title"
}
```

### 5️⃣ Delete a Book (DELETE `/api/books/delete/<id>/`)
**View:** `BookDeleteView`
- Deletes a book entry by ID.

Example request:
```sh
curl -X DELETE http://127.0.0.1:8000/api/books/delete/3/
```

---

## Authentication
The API supports authentication via **JWT tokens**:
1. Obtain a token:
   ```sh
   curl -X POST http://127.0.0.1:8000/api/token-auth/ \
        -H "Content-Type: application/json" \
        -d '{"username": "your_username", "password": "your_password"}'
   ```
2. Use the token for authentication in requests:
   ```sh
   curl -X GET http://127.0.0.1:8000/api/books/ \
        -H "Authorization: Bearer your_token_here"
   ```

---

## Notes
- Ensure that the user making requests has the necessary permissions.
- If the `author` field is `null`, it means the book has no assigned author.
- The API follows RESTful principles, ensuring a clear and structured interaction with book resources.

---

## License
This project is licensed under the MIT License.

