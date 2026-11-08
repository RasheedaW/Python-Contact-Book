
# Store contacts in a dictionary
contacts = {}

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number (10 digits): ").strip()

    if not name:
        print("Name cannot be empty.")
    elif not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number. Enter 10 digits.")
    elif name.lower() in [n.lower() for n in contacts]:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added successfully!")

# View all saved contacts
def view_contacts(contacts):
    if not contacts:
        print("Contact list is empty.")
    else:
        for name, phone in contacts.items():
            print(name + ":", phone)

# Search for a contact
def search_contact(contacts):
    search = input("Enter name to search: ").strip().lower()
    found = False

    for name, phone in contacts.items():
        if search and search in name.lower():
            print(name + ":", phone)
            found = True

    if not found:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    for saved_name in list(contacts):
        if saved_name.lower() == name.lower():
            del contacts[saved_name]
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

# Display the menu repeatedly
while True:
    print("\nContact Book Menu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-5.")

    except ValueError:
        print("Invalid input. Please enter a number.")
