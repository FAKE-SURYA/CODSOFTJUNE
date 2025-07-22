import random
import string

# Function to generate a password
def generate_password(length):
    # Define possible characters: letters, digits, and symbols
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    # Generate a random password
    password = ""
    for _ in range(length):
        password += random.choice(all_chars)
    return password

if __name__ == "__main__":
    print("Welcome to the Simple Password Generator!")
    while True:
        try:
            length = int(input("How long do you want your password to be? (Enter a number, e.g., 12): "))
            if length < 4:
                print("Password should be at least 4 characters long. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    password = generate_password(length)
    print("\nYour generated password is:")
    print(password)
    print("\nThank you for using the Password Generator!")
