def search_contact(all_contacts):
    query = input("Enter name, email, or phone number to search: ")
    results = [contact for contact in all_contacts if query in contact.values()]
    
    if results:
        for contact in results:
            print(f"Found: Name: {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']} | Address: {contact['address']}")
    else:
        print("No matching contact found.")