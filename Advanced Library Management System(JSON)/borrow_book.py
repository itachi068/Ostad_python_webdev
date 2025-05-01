from save_all_books import save_all_books
from datetime import datetime, timedelta
import save_all_borrowers

def borrow_book(all_books, all_borrowers):
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    title = input("Enter book title: ")
    
    # Get current datetime and add 7 days to represent the due date
    due_date = datetime.now() + timedelta(days=7)
    book_borrowed_at = due_date.strftime("%d-%m-%y %H:%M:%S")
    
    borrower = {
        "name": name,
        "phone": phone,
        "title": title,
        "bookBorrowedAt": book_borrowed_at
    }
    all_borrowers.append(borrower)
    save_all_borrowers.save_all_borrowers(all_borrowers)

    # Update book quantity if found
    for book in all_books:
        if book["title"] == title:
            if book.get("quantity", 0) > 0:
                book["quantity"] -= 1
            else:
                print("This book is currently out of stock.")
                return all_books,all_borrowers
            break
    else:
        print("Book not found in the collection.")
        return all_books,all_borrowers
    
    save_all_books(all_books)

    print("\nBook lended till ", book_borrowed_at)

    return all_books,all_borrowers
