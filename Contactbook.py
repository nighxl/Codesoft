def display_menu():
    print("\nContact Book Application")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print("Contact added successfully.")

def view_contacts():
    for name, details in contacts.items():
        print(f"{name}: {details['Phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            print(f"{name}: {details['Phone']}, {details['Email']}, {details['Address']}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep the same): ")
        email = input("Enter new email (leave blank to keep the same): ")
        address = input("Enter new address (leave blank to keep the same): ")
        if phone:
            contacts[name]['Phone'] = phone
        if email:
            contacts[name]['Email'] = email
        if address:
            contacts[name]['Address'] = address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

contacts = {}

while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
