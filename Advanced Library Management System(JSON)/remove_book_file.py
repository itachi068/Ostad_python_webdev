import save_all_books

def delete_book(all_books):
    search_book = input("Enter name of the book to be removed :")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_all_books.save_all_books(all_books)
            print("Book removed succesfully")
            return all_books
        
    print("Book not found!")