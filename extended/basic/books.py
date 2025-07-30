import uvicorn
from fastapi import Body,FastAPI

#app = FastAPI()

### REquest using Get method to fetch data

BOOKS= [
    {'title':'Title One', 'author':'Author One', 'category':'Science'},
    
    {'title':'Title Two', 'author':'Author Two', 'category':'Science Two'},
    
    
    {'title':'Title Three', 'author':'Author Three', 'category':'Science Three'},
    
    
    {'title':'Title Four', 'author':'Author Four', 'category':'Science Four'},
    
    
    {'title':'Title FIVE', 'author':'Author FIVE', 'category':'Science FIVE'},
    
    
    {'title':'Title SIX', 'author':'Author SIX', 'category':'Science SIX'},
    

    {'title':'Title SEVEN', 'author':'Author SEVEN', 'category':'Science SEVEN'},
     
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/get_book_by_author/")
async def get_book_by_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
            
    return books_to_return   

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
            
    return books_to_return        

@app.get("/books/{book_author}/")
async def read_category_by_query(book_author:str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() or book.get('category').casefold() == category.casefold():
                books_to_return.append(book)
    return books_to_return

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
    return {'dynamic_param':dynamic_param}


### Methods to set data and fetch using POST method
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

### PUt request method to update data in the databse it can have a body

@app.put("/book/update_book")
async def update_book(updated_book = Body()):
    for index in range(len(BOOKS)):
        if BOOKS[index].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[index] = updated_book    
@app.delete("/books/delete/{title}")
async def delete_book(title: str):
    for index in range(len(BOOKS)):
        if BOOKS[index].get('title').casefold() == title.casefold():
            BOOKS.pop(index)
            break
     
                    