class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, new_phone or None, new_email or None, new_address or None)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
