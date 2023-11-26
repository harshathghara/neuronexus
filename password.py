import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets based on user preferences
    characters = letters + digits + special_chars

    # Validate that there are enough characters to generate a password
    if len(characters) == 0:
        raise ValueError("Cannot generate password with no character set.")

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def get_user_preferences():
    # Get user preferences for including digits and special characters
    include_digits = input("Include digits in the password? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters in the password? (y/n): ").lower() == 'y'

    return include_digits, include_special_chars

def main():
    print("Welcome to the Password Generator!")

    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Validate that the entered length is a positive integer
    while length <= 0:
        print("Please enter a valid positive length.")
        length = int(input("Enter the desired length of the password: "))

    # Get user preferences for including digits and special characters
    include_digits, include_special_chars = get_user_preferences()

    try:
        # Generate the password
        password = generate_password(length, include_digits, include_special_chars)

        # Display the generated password
        print("Generated Password:", password)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
