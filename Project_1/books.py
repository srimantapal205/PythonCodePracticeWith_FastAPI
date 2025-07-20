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


@app.get("/booksList/{book_title}")
async def get_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"error": "Book not found"}




