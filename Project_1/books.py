from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/booksList")
async def get_books():
    return BOOKS

# @app.get("/booksList/mybook")
# async def get_books():
#     return {"book_title": 'My favorite book'}

# @app.get("/booksList/{dynamic_param}")
# async def get_books(dynamic_param:str):
#     return {"dynamic_param": dynamic_param}

# Get books by title using path parameter
@app.get("/booksList/{book_title}")
async def get_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}


# Get books by category using query parameter
@app.get("/booklist/")
async  def get_read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    if not books_to_return:
        return  {"error": "No books found in this category"}
    return books_to_return


# Get books by author and category using query parameters
@app.get("/booklist/{book_author}/")
async  def get_read_author_category_by_query(book_author: str, category:str):
    book_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get("category").casefold() == category.casefold():
            book_return.append(book)
    if not book_return: return {"error": "No books found for this author in this category"}
    return book_return

# Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
# Get books by author using query parameter
@app.get("/booklist/by_author")
async def get_books_by_author_query(author:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    if not books_to_return:
        return {"error": "No books found for this author"}
    return  books_to_return



# Create a new book using POST method
@app.post("/booksList/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


# Update an existing book using PUT method
@app.put("/booksList/update_book")
async  def update_book(updated_book= Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
    return  {"message": "Book updated successfully", "book": updated_book}


# Delete a book using DELETE method
@app.delete("/booksList/delete_book/{book_title")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
    return {"message": f"Book deleted successfully,", "BOOKS":BOOKS}

