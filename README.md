# Python Username & Password Registration Program

This Python program allows a user to set up a username and password with certain requirements. It serves as a basic example of how a registration system might be implemented.



## Features
- Username input: Allows the user to set their desired username.
- Password input: Allows the user to set their password, ensuring  it's at least 12 characters long.
- Password verification: Asks the user to re-enter their password, verifying they know it, and provides opportunity for correction in case of mismatch.


## Algoritm

![Alt text]([![](https://mermaid.ink/img/pako:eNqFkU9rwzAMxb-K0bk9bMfAOhjNoTDGINtgkIuwlT9Q20GyGSXJd5_XJFsDgflkSb_3Hkg9aG8IMqgZu0a9PZVOpVcE5KD2-4PKXSB-F2KHlqbhqvUHvaLIl2dzAy2tK3SSpXz2rs6dj3UzsVuT_iSqW-SHB3V3r3SDjDrZyuN4dRxe_LCVveU3CT5JBvVB3FaXtWTd64_-N1yUxaCbfyLX-puwImpNIvNap2LeWZLCDiyxxdakE_Q_UAmhobRpyNLXUIXxHEoo3ZjQ2BkMlJs2eIaswrPQDjAGX1ychixwpAU6tpguamdq_AakHqhi?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqFkU9rwzAMxb-K0bk9bMfAOhjNoTDGINtgkIuwlT9Q20GyGSXJd5_XJFsDgflkSb_3Hkg9aG8IMqgZu0a9PZVOpVcE5KD2-4PKXSB-F2KHlqbhqvUHvaLIl2dzAy2tK3SSpXz2rs6dj3UzsVuT_iSqW-SHB3V3r3SDjDrZyuN4dRxe_LCVveU3CT5JBvVB3FaXtWTd64_-N1yUxaCbfyLX-puwImpNIvNap2LeWZLCDiyxxdakE_Q_UAmhobRpyNLXUIXxHEoo3ZjQ2BkMlJs2eIaswrPQDjAGX1ychixwpAU6tpguamdq_AakHqhi))
![image](https://github.com/Chinilshik-kalkulatorov/Gay_test/assets/95532146/5363135d-c778-42d0-a8fb-ba4634a86199)




## Usage/Examples


Run the script in your Python environment. The program will guide you through the registration process.

```Python
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if len(password) < 12:  # Check password length
        print("Password must be at least 12 characters. Please try again.")
        continue  # Return to start of loop

    password_check = input("Re-enter your password: ")

    if password == password_check:  # Check password match
        print("Registration successful.")
        break
    else:
        print("Passwords do not match. Please try again.")
```


## Run Locally

Run the script in your Python environment. The program will guide you through the registration process.

```bash
  python Testmile.py
```


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

