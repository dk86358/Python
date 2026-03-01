def decimal_to_binary():
    while True:
        try:
            # Ask user for input
            number = int(input("Enter a decimal number between 0 and 255: "))

            # Check if number is within range
            if number < 0 or number > 255:
                print("Error: Only numbers between 0 and 255 are acceptable.")
            else:
                # Convert to binary
                binary = bin(number)[2:]   # Remove '0b' prefix
                print(f"The binary equivalent of {number} is {binary}")

        except ValueError:
            print("Error: Please enter a valid integer.")

        # Ask user if they want to continue
        again = input("Would you like to convert another number? (yes/no): ").lower()

        if again != "yes":
            print("Program ended.")
            break


# Run the program
decimal_to_binary()