from fastapi import FastAPI

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


# Get books by category using query parameter
@app.get("/booklist/{book_author}/")
async  def get_read_author_category_by_query(book_author: str, category:str):
    book_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get("category").casefold() == category.casefold():
            book_return.append(book)
    if not book_return: return {"error": "No books found for this author in this category"}
    return book_return


