import restore_all_borrowers
import borrow_book
import return_book

def borrowing_file(all_books):
    all_borrowers = []

    while True:
        print("\n--- Borrow / Return Menu ---")
        print("0. Exit")
        print("1. Borrow book")
        print("2. Return book")

        all_borrowers = restore_all_borrowers.restore_all_borrowers(all_borrowers)

        menu = input("Select any number: ")

        if menu == "0":
            print("Exiting Borrow/Return menu.")
            break
        elif menu == "1":
            all_books, all_borrowers = borrow_book.borrow_book(all_books, all_borrowers)
        elif menu == "2":
            all_books, all_borrowers = return_book.return_book(all_books, all_borrowers)
        else:
            print("Choose a valid number.")
