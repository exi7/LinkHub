import time
import os
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
g = Fore.LIGHTGREEN_EX

def choice2():
    # Load all contacts from the file
    with open('directory.txt', 'r') as f:
        lines = f.readlines()

    # Display the list of saved contact names
    if lines:
        print("Here is the list of saved contacts:")
        for i, line in enumerate(lines, 1):
            name = line.split(' ')[0]  # Extract just the name
            print(f"{i}. {name}")
    else:
        print("The directory is empty.")
        time.sleep(3)
        menu()
        return

    search = input("\nWould you like to search by name (1) or by number (2)? : ")
    
    if search == '1':  
        name = input("Who are you looking for? : ")
        found_contacts = [line.strip() for line in lines if line.startswith(name + ' ')]
        
        if found_contacts:
            print(f"Contacts found for {name}:\n")
            for contact in found_contacts:
                print(contact)
                
            contact_file = f"Contacts/{name}.txt"
            if os.path.exists(contact_file):
                print("\nContact details:")
                with open(contact_file, 'r') as f:
                    print(f.read())
        else:
            print(f"{name} is not saved in your directory!")
        time.sleep(3)
        menu()
    
    elif search == '2':  
        number = input("Which number are you looking for? : ")
        found_contacts = [line.strip() for line in lines if number in line]
        
        if found_contacts:
            print(f"Contacts found for number {number}:\n")
            for contact in found_contacts:
                print(contact)
        else:
            print(f"{number} is not saved in your directory!")
        
        time.sleep(3)
        menu()
    else:
        print("Invalid option. Please choose 1 or 2.")
    menu()

def choice1():
    name = input('Enter a name: ')
    number = input('Enter the number associated with this name: ')
    
    info = f"{name} {number}"
    categories = {}
    
    while True:
        category = input("Enter an additional category (e.g., Address, Email, Job, Discord) or press Enter to finish: ")
        if not category.strip():
            break
        value = input(f"Enter the value for {category}: ")
        categories[category] = value
        info += f" | {category}: {value}"
    
    with open('directory.txt', 'a') as f:
        f.write(info + '\n')

    if not os.path.exists("Contacts"):
        os.makedirs("Contacts")
    
    with open(f"Contacts/{name}.txt", 'w') as f:
        f.write(f"Name: {name}\nNumber: {number}\n")
        for category, value in categories.items():
            f.write(f"{category}: {value}\n")
    
    print(f"{name} has been added to the directory with the following information: {info}")
    time.sleep(3)
    menu()

def choice3():
    name = input("Enter the name of the person to modify: ")
    with open('directory.txt', 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if line.startswith(name + ' '):
            print(f"Current information: {line.strip()}")
            
            new_name = input("Enter the new name (or press Enter to keep the old one): ") or name
            new_number = input("Enter the new number (or press Enter to keep the old one): ") or line.split(' ')[1]
            
            existing_categories = {c.split(' : ')[0]: c.split(' : ')[1] for c in line.strip().split(" | ")[2:] if " : " in c}
            
            while True:
                action = input("Modify an existing category (1), add a new category (2), or finish (3)? : ")
                if action == '1':
                    category_to_modify = input("Enter the name of the category to modify: ")
                    if category_to_modify in existing_categories:
                        new_value = input(f"Enter the new value for {category_to_modify}: ")
                        existing_categories[category_to_modify] = new_value
                    else:
                        print("This category does not exist.")
                elif action == '2':
                    new_category = input("Enter the new category name: ")
                    new_value = input(f"Enter the value for {new_category}: ")
                    existing_categories[new_category] = new_value
                elif action == '3':
                    break
                else:
                    print("Invalid option.")
            
            new_info = f"{new_name} {new_number}"
            for category, value in existing_categories.items():
                new_info += f" | {category}: {value}"
            
            lines[i] = new_info + '\n'
            with open('directory.txt', 'w') as f:
                f.writelines(lines)
            
            os.makedirs("Contacts", exist_ok=True)
            with open(f"Contacts/{new_name}.txt", 'w') as f:
                f.write(f"Name: {new_name}\nNumber: {new_number}\n")
                for category, value in existing_categories.items():
                    f.write(f"{category}: {value}\n")
            
            print(f"{name}'s information has been updated.")
            time.sleep(3)
            menu()
    
    print(f"{name} is not in the directory!")
    time.sleep(1)
    print("Returning to menu!")
    menu()

def choice0():
    print("Thank you for using the directory. See you next time!")
    time.sleep(1)
    exit()

def menu():
    choice = int(input(f""" 
                {g}
                 ██▓     ██▓ ███▄    █  ██ ▄█▀ ██░ ██  █    ██  ▄▄▄▄   
                ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ ▓██░ ██▒ ██  ▓██▒▓█████▄ 
                ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ ▒██▀▀██░▓██  ▒██░▒██▒ ▄██
                ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
                ░██████▒░██░▒██░   ▓██░▒██▒ █▄░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
                ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
                 ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
                  ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░  ░  ░░ ░ ░░░ ░ ░  ░    ░ 
                    ░  ░ ░           ░ ░  ░    ░  ░  ░   ░      ░      
                                                     ░ 
{g}------------------------------------------------------------------------------------------------------------------------\n{w}https://github.com/exi7 {b}|{w} https://github.com/exi7 {b}|{w} https://github.com/exi7 {b}|{w} https://github.com/exi7 {b}|{w} https://github.c\n{g}------------------------------------------------------------------------------------------------------------------------\n{w}
 {g}┌                                                                                              
 ├           ┌─────────────────┐       
 └─┬─────────┤   {w}Directory{g}    ├
   │         └─────────────────┘         
   ├─ [{w}1{g}] Register a new contact
   ├─ [{w}2{g}] View contact information
   ├─ [{w}3{g}] Modify contact information 
   └─ [{w}0{g}] Exit               
                  

    Enter your choice: """))

    if choice == 0:
        choice0()
    elif choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    elif choice == 3:
        choice3()
    else:
        print("Invalid option. Please select a valid option.")
    
menu()
