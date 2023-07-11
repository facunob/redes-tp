import requests, json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#DB
response = requests.get('https://github.com/benoitvallon/100-best-books/raw/master/books.json')
database_no_id = json.loads(response.content)
database = []
for i in range(len(database_no_id)):
    book = database_no_id[i]
    book["id"] = i
    database.append(book)


#APP
app = FastAPI()


@app.get("/api")
def listar():
    return database


def find_book_by_id(id):
    id = int(id)
    book = None
    for x in database:
        print(id, x.get("id"))
        if int(x.get("id")) == id:
            book = x
            break
    return book


@app.get("/api/{id}")
def listar(id):
    book = find_book_by_id(id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

class Book(BaseModel):
    id: int = None
    author: str
    title: str = None
    country: str = None
    imageLink: str = None
    language: str = None
    link: str = None
    pages: str = None
    year: int = None

@app.post("/api")
def add_character(new_book: Book):
    new_id = max([x.get("id") for x in database]) + 1
    book = {
        "id": new_id,
        "author": new_book.author,
        "title": new_book.title,
        "country": new_book.country,
        "imageLink": new_book.imageLink,
        "language": new_book.language,
        "link": new_book.link,
        "pages": new_book.pages,
        "year": new_book.year,
    }
    database.append(book)
    return book

@app.put("/api/{id}")
def add_character(id, new_book: Book):
    book = find_book_by_id(id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found")
    database.remove(book)
    book = {
        "id": book.get("id"),
        "author": new_book.author,
        "title": new_book.title,
        "country": new_book.country,
        "imageLink": new_book.imageLink,
        "language": new_book.language,
        "link": new_book.link,
        "pages": new_book.pages,
        "year": new_book.year,
    }
    database.append(book)
    return book

@app.delete("/api/{id}")
def delete_by_id(id):
    book = find_book_by_id(id)
    if book == None:
        raise HTTPException(status_code=404, detail="Book not found")
    database.remove(book)
    return book