import save_all_books
from datetime import datetime

def update_books(all_books):
    search_book = input("Enter name of the book :")
    for book in all_books:
        if book["title"] == search_book:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter book publishing year: "))
            price = int(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))
            bookUpdatedAt = datetime.now().strftime("%d-%m-%y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookUpdatedAt"] = bookUpdatedAt
            
            save_all_books.save_all_books(all_books)
            print("Books Updated succesfully")
            return all_books
        
    print("Book not found!")