#TO-Do List
user_input = 0
data = list()

while user_input != "4":
    print("Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View items")
    print("4. Exit")  

    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        item = input("Enter the item to be added: ")
        data.append(item)
        print("Item added to list: ", item)
    
    elif user_input == "2":
        item = input("Enter the item to be removed: ")
        if item in data:
            data.remove(item)
            print("Removed item: ", item)
        else:
            print(item, "does not exist in the To-Do List")
    
    elif user_input == "3":
        print("To-Do List:")
        if data:
            for item in data:
                print(item)
        else:
            print("The list is empty.")
    
    elif user_input == "4":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice, please enter a number between 1 and 4")
