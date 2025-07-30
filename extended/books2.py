import uvicorn
from pydantic import BaseModel
from fastapi import Body,FastAPI,Path, Query,HTTPException
from Book import *
from BookRequest import *
from starlette import status

app = FastAPI()

BOOKS = [
Book(id=1, title='Welcome to FASTAPI', author='CodingWithMody', description='A very nice book', rating=5, published_date= 2012),
Book(id=2, title='Mastering Python', author='John Doe', description='An in-depth Python guide', rating=4, published_date= 2014),
Book(id=3, title='Async Programming in Python', author='Jane Smith', description='Learn asyncio and concurrency', rating=4, published_date= 2015),
Book(id=4, title='FastAPI in Action', author='Alice Johnson', description='Practical FastAPI usage', rating=5, published_date= 2012),
Book(id=5, title='Database Design Basics', author='Bob Lee', description='Learn the fundamentals of databases', rating=3, published_date= 2014),
Book(id=6, title='Deploying Python Apps', author='Dev Ops Pro', description='Guide to deploy Python web apps', rating=4, published_date= 2016),
Book(id=7, title='REST APIs with FastAPI', author='Mody Team', description='Build robust APIs with FastAPI', rating=5, published_date= 2018),
Book(id=8, title='Modern Web Development', author='Sarah Connor', description='Full-stack guide for beginners', rating=4, published_date= 2015),
Book(id=9, title='Clean Code in Python', author='Robert Martin Jr.', description='Best practices for writing clean code', rating=5, published_date= 2012),
Book(id=10, title='Python Data Science Handbook', author='Jake VanderPlas', description='Essential tools for data science', rating=5, published_date= 2012),
    
]

@app.get("/books",status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/read_book_by_date/",status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(publish_date: int = Query(gt=1999,lt=2026)):
    books_to_return= []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)
    return books_to_return 


@app.get("/books/,status_code=status.HTTP_200_OK")
async def read_books_by_rating(book_rating: int = Query(gt=0,lt=6)):
    books_to_return= []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return        


@app.get("/books/{bookId}",status_code=status.HTTP_200_OK)
async def read_book(bookId: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == bookId:
         return book
    raise HTTPException(status_code=404,detail='Item not found bro') 

@app.post("/create-book",status_code=status.HTTP_201_CREATED)
async def create_book(book_Request: BookRequest):
    new_book = Book(**book_Request.model_dump())
    BOOKS.append(find_book_id(new_book))

@app.put("/books/update-book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i]= book
            book_changed= True
    if not book_changed:        
        raise HTTPException(status_code=404,detail='Book not found!')    
        
@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed=True
            break        
    if not book_changed:        
        raise HTTPException(status_code=404,detail='Book not found!')            
        
       
    
def find_book_id(book: Book)-> Book:
    # if len(BOOKS) > 0:
    #     book.id= BOOKS[-1].id +1
    # else:
    #     book.id = 1    
    # return book    
    book.id = 1 if len(BOOKS)==0 else BOOKS[-1].id +1
    return book  