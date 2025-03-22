def view_contacts(all_contacts):
    if all_contacts:
        for contact in all_contacts:
            print(f"Name: {contact['name']} | Email: {contact['email']} | Phone: {contact['phone']} | Address: {contact['address']}")
    else:
        print("No contacts found.")