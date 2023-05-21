username = input("Enter username: ")  # Prompt user for username
password = input("Enter password: ")  # Prompt user for password


if username == 'Alan':  # Check password length
    print("Why are you gay?")
    if input("Who says I am gay?"):
         print("You are gay.")
    else:
        print("You are not gay")

    password_check = input("Re-enter your password: ")  # Ask user to verify password

    if password == password_check:  # Check password match
        print("Registration successful.")
        break  # If all is well, break loop
    else:
        print("Passwords do not match. Please try again.")
