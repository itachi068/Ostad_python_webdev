import add_contact
import view_contacts
import remove_contact
import search_contact

all_contacts = []

while True:
    print("Welcome to Contact Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    
    menu = input("Select an option: ")
    
    if menu == "0":
        print("Thanks for using Contact Management System")
        break
    elif menu == "1":
        all_contacts = add_contact.add_contact(all_contacts)
    elif menu == "2":
        view_contacts.view_contacts(all_contacts)
    elif menu == "3":
        all_contacts = remove_contact.remove_contact(all_contacts)
    elif menu == "4":
        search_contact.search_contact(all_contacts)
    else:
        print("Choose a valid option")