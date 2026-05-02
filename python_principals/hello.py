# Greet the user
print("Hello! Welcome to the Basic Interaction Program.")

name = input("What's your name? ").strip()
if not name:
    name = "User"

print(f"Nice to meet you, {name}!")

numbers = []

while True:
    print("\nOptions:")
    print("1. Add a number to the list")
    print("2. View the list")
    print("3. Calculate sum")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        num_str = input("Enter a number: ").strip()
        if num_str.isdigit():
            numbers.append(int(num_str))
            print("Number added!")
        else:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        if numbers:
            print("Your numbers:")
            for num in numbers:
                print(num)
        else:
            print("The list is empty.")
    elif choice == "3":
        if numbers:
            total = sum(numbers)
            print(f"The sum is: {total}")
        else:
            print("No numbers to sum.")
    elif choice == "4":
        print(f"Goodbye, {name}!")
        break
    else:
        print("Invalid choice. Please select 1-4.")