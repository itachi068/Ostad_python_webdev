from save_contacts import save_contacts

def remove_contact(all_contacts):
    phone = input("Enter phone number to delete: ")
    
    updated_contacts = [contact for contact in all_contacts if contact["phone"] != phone]
    
    if len(updated_contacts) == len(all_contacts):
        print("No contact found with that phone number.")
    else:
        save_contacts(updated_contacts)
        print("Contact deleted successfully!")
    
    return updated_contacts