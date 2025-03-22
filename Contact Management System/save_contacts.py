def save_contacts(all_contacts):
    with open("contacts.csv", "w") as file:
        for contact in all_contacts:
            line = f"{contact['name']}, {contact['email']}, {contact['phone']}, {contact['address']}\n"
            file.write(line)