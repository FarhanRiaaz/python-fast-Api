````markdown
# 📚 Book CRUD API with FastAPI

This is a simple CRUD (Create, Read, Update, Delete) REST API built using **FastAPI**. The app manages a list of books stored in a hardcoded in-memory list. It's ideal for beginners who want to learn how API endpoints work in FastAPI.

> 🔗 [GitHub Repository](https://github.com/FarhanRiaaz/python-fast-Api.git)

---

## 🚀 Features

- 📖 View all books
- 🔍 Search book by **title**
- 🔍 Filter books by **category** or **author**
- ➕ Add a new book
- 📝 Update a book
- ❌ Delete a book

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn** (for running the server)

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/FarhanRiaaz/python-fast-Api.git
   cd python-fast-Api
````

2. **Create and activate a virtual environment (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install fastapi uvicorn
   ```

---

## ▶️ Running the App

```bash
uvicorn main:app --reload
```

The app will run on: [http://127.0.0.1:8000](http://127.0.0.1:8000)

You can also access the **interactive API docs** at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 API Endpoints

### ✅ `GET /books`

Returns a list of all books.

### ✅ `GET /books/{book_title}`

Returns book details by title (case-insensitive).

### ✅ `GET /books/?category=Science`

Returns books filtered by category.

### ✅ `GET /books/{book_author}/?category=Science`

Returns books that match the given author or category.

### ✅ `POST /books/create_book`

Adds a new book.

**Request Body:**

```json
{
  "title": "New Book",
  "author": "New Author",
  "category": "New Category"
}
```

### ✅ `PUT /book/update_book`

Updates a book by matching the title.

**Request Body:**

```json
{
  "title": "Title One",
  "author": "Updated Author",
  "category": "Updated Category"
}
```

### ✅ `DELETE /books/delete/{title}`

Deletes a book by its title.

---

## ⚠️ Notes & Limitations

* 📌 Data is **not persistent** — all changes are lost on server restart.
* ⚠️ Route `/books/{dynamic_param}` may conflict with `/books/{title}` – consider refactoring.
* 📥 No schema validation yet — a good next step would be using **Pydantic models**.

---

## 📚 Sample Book Object

```json
{
  "title": "Title One",
  "author": "Author One",
  "category": "Science"
}
```

---

## 🧠 What You’ll Learn

* FastAPI routing and endpoint creation
* Handling GET, POST, PUT, DELETE methods
* Using query parameters and path variables
* Sending and receiving request bodies

---

## 🚧 What's Next?

* [ ] Add **Pydantic models** for request validation
* [ ] Integrate a database (e.g., SQLite or PostgreSQL)
* [ ] Add **status codes** and **error handling**
* [ ] Refactor routes for better clarity
* [ ] Deploy using **Render**, **Railway**, or **Vercel**

---

## 👨‍💻 Author

**Farhan Riaaz**
[GitHub Profile →](https://github.com/FarhanRiaaz)

---

### ⭐️ If you find this helpful, give it a star!

```

---
```
