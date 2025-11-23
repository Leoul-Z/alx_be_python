def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            while True:
                item = input("Enter the item name to remove: ")
                if item not in shopping_list:
                    print("Item is not found")
                else:
                    shopping_list.remove(item)
                    break
            pass
        elif choice == '3':
            for i in range(0, len(shopping_list)):
                print(shopping_list[i])
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
