from save_all_books import save_all_books
import random
from datetime import datetime


def add_books(all_books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    # isbn = int(input("Enter book isbn: "))
    #we will now create a random isbn rather than taking input 
    year = int(input("Enter book publishing year: "))
    price = int(input("Enter book price: "))
    
    while True:
        try:
           quantity = int(input("Enter book quantity: "))
           break
        except ValueError:
            print("Please enter a valid integer number") 
            

    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    bookUpdatedAt = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    book={
        "title" : title,
        "author" : author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt":bookAddedAt,
        "bookUpdatedAt":bookUpdatedAt
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books added succesfully")
    
    return all_books