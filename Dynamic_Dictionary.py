dictionary = {}


def add_words():
    key = input("Enter the key: ")
    if key in dictionary:
        value = input("Enter value: ")
        if dictionary[key] == value:
            print(f"Key {key} already has the same value {value}")
        else:
            print(f"Key {key} has a different value {dictionary[key]}")
            change_value = input(
                f"Do you want to change the value for key {key}? (y/n): "
            )
            if change_value.lower() == "y":
                dictionary[key] = value
                print(f"Value for key {key} changed to {value}")
            else:
                print(f"Value for key {key} not changed")
    else:
        value = input("Enter value: ")
        dictionary[key] = value
        print(f"Key {key} added with value {value}")


def menu():
    print("1: Add words")
    print("2: Looking for")
    print("3: Remove words")
    print("4: Show dict")
    print("q: Quit")

    while True:
        choice = input("What do you want?: ")

        if choice == "q":
            break
        elif choice == "1":
            add_words()
        elif choice == "2":
            looking_for_key(input("What are you looking for?: "))
        elif choice == "3":
            remove_key(input("Which key do you want to remove?: "))
        elif choice == "4":
            print(dictionary)
        else:
            print("I say! WHAT DO YOU WANT?")


def looking_for_key(key):
    if key in dictionary:
        print(f"Key: {key}, Value: {dictionary[key]}")
    else:
        print("Key not found")


def remove_key(key):
    if key in dictionary:
        del dictionary[key]
        print(f"Key: {key} removed from the dictionary")
    else:
        print(f"Key: {key} not found in the dictionary")


menu()
