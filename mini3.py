import re

contacts = {}

def add_contact():
    email = input("Enter contact's email: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        if email in contacts:
            print("This email already exists.")
        else:
            name = input("Enter contact's name: ")
            phone = input("Enter contact's phone number: ")
            additional_info = input("Enter additional information (optional): ")
            contacts[email] = {
                'Name': name,
                'Phone': phone,
                'Additional Info': additional_info
            }
            print("Contact added successfully!")
    else:
        print("Invalid email format.")

