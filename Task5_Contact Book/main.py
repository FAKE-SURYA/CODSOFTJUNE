import sys

# Contact structure: list of dicts
contacts = []

def add_contact():
    print("\nAdd New Contact")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    print("\nContact List:")
    if not contacts:
        print("No contacts found.")
        return
    print(f"{'No.':<4} {'Name':<20} {'Phone':<15}")
    print("-"*45)
    for idx, c in enumerate(contacts, 1):
        print(f"{idx:<4} {c['name']:<20} {c['phone']:<15}")

def search_contact():
    print("\nSearch Contact")
    query = input("Enter name or phone number to search: ").strip().lower()
    found = False
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    print("\nUpdate Contact")
    name = input("Enter the name of the contact to update: ").strip().lower()
    for c in contacts:
        if c['name'].lower() == name:
            print(f"Current details: {c}")
            c['name'] = input(f"New Name [{c['name']}]: ") or c['name']
            c['phone'] = input(f"New Phone [{c['phone']}]: ") or c['phone']
            c['email'] = input(f"New Email [{c['email']}]: ") or c['email']
            c['address'] = input(f"New Address [{c['address']}]: ") or c['address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name:
            print(f"Deleting contact: {c['name']}")
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Welcome to the Contact Book!")
    main_menu()

