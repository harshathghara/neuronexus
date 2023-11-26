class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, keyword):
        matching_contacts = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if not matching_contacts:
            print(f"No contacts found with '{keyword}'.")
        else:
            print(f"Matching contacts for '{keyword}':")
            for i, contact in enumerate(matching_contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def update_contact(self, contact_index, new_contact):
        self.contacts[contact_index] = new_contact
        print("Contact updated successfully.")

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]
        print("Contact deleted successfully.")


def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def get_contact_details():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    return Contact(name, phone, email, address)


def main():
    contact_manager = ContactManager()

    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact_manager.add_contact(get_contact_details())
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_manager.search_contact(keyword)
        elif choice == '4':
            contact_manager.view_contacts()
            index = int(input("Enter the index of the contact to update: ")) - 1
            new_contact = get_contact_details()
            contact_manager.update_contact(index, new_contact)
        elif choice == '5':
            contact_manager.view_contacts()
            index = int(input("Enter the index of the contact to delete: ")) - 1
            contact_manager.delete_contact(index)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
