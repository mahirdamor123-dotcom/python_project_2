print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\n======== MENU ========")
    print("1. Generate Pattern")
    print("2. Analyze the range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        rows_input = input("Enter the number of rows for the pattern: ")

        try:
            rows = int(rows_input)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if rows <= 0:
            print("Invalid rows count! Please enter a positive integer.")
            continue

        print("Pattern:")
        for i in range(1, rows + 1):
            print("*" ,end="  ")
        print()  # Move to the next line after printing the pattern

    elif choice == '2':
        start_input = input("Enter the starting number: ")
        end_input = input("Enter the ending number: ")

        try:
            start = int(start_input)
            end = int(end_input)
        except ValueError:
            print("Invalid input! Please enter valid integers.")
            continue

        if start > end:
            print("Invalid range! Starting number should be less than or equal to ending number.")
            continue

        print(f"Analyzing numbers from {start} to {end}:")
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"{num} is even.")
            else:
                print(f"{num} is odd.")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a valid option (1-3).")

