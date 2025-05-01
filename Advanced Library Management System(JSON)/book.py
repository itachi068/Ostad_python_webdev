import add_books
import view_all_books
import restore_all_books
import update_books
import remove_book_file
import borrow

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View all books")
    print("3. Update books")
    print("4. Delete books")
    print("5. Borrow/return books")
    
    all_books = restore_all_books.restore_all_books(all_books)
    
    menu = input("select any number: ")
    
    if menu=="0":
        print("Thanks for using Library Management System")
        break
    elif menu =="1":
        all_books = add_books.add_books(all_books)
    elif menu =="2":
        view_all_books.view_all_books(all_books)
    elif menu =="3":
        update_books.update_books(all_books)
    elif menu =="4":
        remove_book_file.delete_book(all_books)
    elif menu =="5":
        borrow.borrowing_file(all_books)
    else:
        print("Choose a valid number")
        
        