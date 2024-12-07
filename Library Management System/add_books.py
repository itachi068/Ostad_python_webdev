from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = int(input("Enter book isbn: "))
    year = int(input("Enter book publishing year: "))
    price = int(input("Enter book price: "))
    quantity = int(input("Enter book quantity: "))
    
    book={
        "title" : title,
        "author" : author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books added succesfully")
    
    return all_books