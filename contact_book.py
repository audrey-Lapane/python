#Stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts. This is a foundational data structure pattern used in virtually every real app.

contacts = []
#function to add contacts
def add_contact():
    name = input("Enter contact's name:").lower()
    phone = input("Enter contact's number:")
    email = input("Enter contact's email:")
    store_contacts = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }
    contacts.append(store_contacts)
    print("Contact added successfully!\n")

#function to search contacts
def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None
    
#function to delete contacts
def delete_contact(name):
    contact = search_contact(name)

    if contact in contacts:
        contacts.remove(contact)
        print(f"{name} is deleted successfully from the contact\n")
    else:
        print("Contact not found\n")

#function to view contacts
def view_all():
    if len(contacts) == 0:
        print("You have 0 contacts")

    else:
        print("--------Contact List-------")
        print("{:<20} {:<15} {:<30}".format("Name", "Phone", "Email"))
        print("-" * 65)

        for contact in contacts:
            print("{:<20} {:<15} {:<30}".format(
                contact["name"],
                contact["phone"],
                contact["email"]
            ))


while True:
    choice = int(input("choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)"))

    if choice == 1:
        add_contact()
    elif choice == 2:
        name = input("search contacts by name: ").lower()
        result = search_contact(name)

        if result:
            print("\nContact Found:")
            print("Name :", result["name"])
            print("Phone:", result["phone"])
            print("Email:", result["email"])
            print()
        else:
            print("Contact not found.\n")
    elif choice == 3:
        name = input("Delete contact by name: ").lower()
        delete_contact(name)
    elif choice == 4:
        view_all()
    elif choice == 5:
        break
