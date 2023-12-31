class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, keyword):
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def update_contact(self, name, new_phone_number):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = new_phone_number
                print("Contact updated successfully.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")

def main():
    contacts = ContactList()
    while True:
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contacts.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contacts.view_contact_list()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            contacts.search_contact(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter the new phone number: ")
            contacts.update_contact(name, new_phone_number)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contacts.delete_contact(name)

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
