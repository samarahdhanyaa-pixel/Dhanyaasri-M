shopping_list = []

while True:
    print("1. Add item")
    print("2. Show list")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print("Item added")

    if choice == "2":
        print("Shopping List:", shopping_list)

    if choice == "3":
        print("Exiting program")
        break
