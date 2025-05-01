import save_all_books
import save_all_borrowers

def return_book(all_books, all_borrowers):
    search_name = input("Enter your name: ")
    search_book = input("Enter title of the book to be returned: ")

    borrower_found = False

    for borrower in all_borrowers:
        if borrower["name"] == search_name and borrower["title"] == search_book:
            all_borrowers.remove(borrower)
            save_all_borrowers.save_all_borrowers(all_borrowers)
            borrower_found = True
            break

    if not borrower_found:
        print("No matching borrower record found.")
        return all_books, all_borrowers

    for book in all_books:
        if book["title"] == search_book:
            book["quantity"] = book.get("quantity", 0) + 1
            save_all_books.save_all_books(all_books)
            print("Book returned successfully.")
            break
    else:
        print("Book not found in the library records.")

    return all_books, all_borrowers
