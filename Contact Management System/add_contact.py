from save_contacts import save_contacts

def add_contact(all_contacts):
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    
    if not name.isalpha():
        print("Error: Name must be a string.")
        return all_contacts
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return all_contacts
    
    for contact in all_contacts:
        if contact["phone"] == phone:
            print("Error: Phone number already exists.")
            return all_contacts
    
    contact = {"name": name, "email": email, "phone": phone, "address": address}
    all_contacts.append(contact)
    save_contacts(all_contacts)
    
    print("Contact added successfully!")
    return all_contacts