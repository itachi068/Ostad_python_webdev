# contact_manager.py
import os
import csv

class ContactManager:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.contacts = [row for row in reader]
    
    def save_contacts(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['Name', 'Email', 'Phone Number', 'Address']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.contacts)

    def add_contact(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")

        if not name.isalpha():
            print("Error: Name must be a string.")
            return
        if not phone.isdigit():
            print("Error: Phone number must be numeric.")
            return
        if any(contact['Phone Number'] == phone for contact in self.contacts):
            print("Error: Phone number already exists.")
            return

        self.contacts.append({
            'Name': name,
            'Email': email,
            'Phone Number': phone,
            'Address': address
        })
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print(f"{'Name':<20}{'Email':<30}{'Phone Number':<15}{'Address':<30}")
        print("="*95)
        for contact in self.contacts:
            print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone Number']:<15}{contact['Address']:<30}")

    def remove_contact(self):
        phone = input("Enter the phone number of the contact to remove: ")
        for contact in self.contacts:
            if contact['Phone Number'] == phone:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact removed successfully.")
                return
        print("Error: Contact not found.")

    def search_contact(self):
        query = input("Enter search term (name, email, phone, or address): ").lower()
        results = [contact for contact in self.contacts if query in contact['Name'].lower() or
                   query in contact['Email'].lower() or
                   query in contact['Phone Number'].lower() or
                   query in contact['Address'].lower()]
        if results:
            print(f"{'Name':<20}{'Email':<30}{'Phone Number':<15}{'Address':<30}")
            print("="*95)
            for contact in results:
                print(f"{contact['Name']:<20}{contact['Email']:<30}{contact['Phone Number']:<15}{contact['Address']:<30}")
        else:
            print("No contacts found matching the query.")
