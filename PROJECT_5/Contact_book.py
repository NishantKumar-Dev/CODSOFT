class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("No matching contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if phone: contact.phone = phone
                if email: contact.email = email
                if address: contact.address = address
                print(f"Contact for {name} updated successfully.")
                return
        print(f"Contact for {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact for {name} deleted successfully.")
                return
        print(f"Contact for {name} not found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_book = ContactBook()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(name, phone, email, address)
        
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
