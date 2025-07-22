from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author:str
    description: str
    rating: int
    published_date:int
    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID of the book, auto-generated if not provided', default=None)
    title: str = Field( min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=10, max_length=200)
    rating: int = Field(gt=0, lt=6)  # Rating must be between 1 and 5
    published_date : int = Field(gt=1999, lt=2031)
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A New Book",
                "author": "Name Of Author",
                "description": "This is a description of the book.",
                "rating": 5,
                'published_date':2029
            }
        }
    }

# In-memory storage for books
BOOKS = [
    Book(1, "1984", "George Orwell", "Dystopian novel set in totalitarian society", 5, 2001 ),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "Novel about racial injustice in the Deep South", 4 , 2010),
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald", "Story of the Jazz Age in the United States", 4 , 2001),
    Book(4, "Pride and Prejudice","Jane Austen", "Romantic novel about manners and marriage", 5 , 2011),
    Book(5, "The Catcher in the Rye", "J.D. Salinger", "Novel about teenage angst and alienation", 4 , 2023),
    Book(6, "Brave New World", "Aldous Huxley", "Dystopian novel about a technologically advanced future", 5, 2015   )

]

""""
{
"id": 7,
"title": "Fahrenheit 451",
"author": "Ray Bradbury",
"description": "Dystopian novel about a future where books are banned",
"rating": 5
}
"""
# Get all books
@app.get("/books")
async  def get_books():
    return BOOKS


# Get a book by ID
@app.get("/books/{book_id}")
async  def get_book_by_id(book_id : int):
    for book in BOOKS:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}


# filter books by rating
@app.get("/books/")
async  def get_book_by_rating(book_rating: int):
    book_to_return = []
    if book_rating <1 or book_rating > 5:
        return {"error": "Rating must be between 1 and 5"}
    for book in BOOKS:
        if book.rating == book_rating:
            book_to_return.append(book)
    if len(book_to_return) == 0:
        return {"error": "No books found with the specified rating"}
    return book_to_return

#filter books by published date
@app.get("/books/publish/")
def get_book_by_published_date(published_date: int):
    book_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            book_to_return.append(book)
    if not  book_to_return:
        return {"error": "No books found with the specified published date"}
    return book_to_return




# Using Body to accept raw JSON input
@app.post("/create_book_body")
async  def create_book(book_request = Body()):
    BOOKS.append(book_request)


#Using Pydantic model for structured input
@app.post("/create_book")
async  def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id+1
    # if len(BOOKS)>0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    return  book


# Update a book id
# @app.put("/books/update_book/{book_id}")
# async def update_book(book: BookRequest):
#     for b in range(len(BOOKS)):
#     # Check if the book with the given ID exists
#         if BOOKS[b].id == book.id:
#             print(BOOKS[b])
#             BOOKS[b] = Book(**book.model_dump())
#

#Delete a book by ID
@app.delete("/books/{book_id}")
async  def delete_book(book_id:int):
    for b in range(len(BOOKS)):
        if BOOKS[b].id == book_id:
            BOOKS.pop(b)
            break
    return  {"message": "Book deleted successfully"}


