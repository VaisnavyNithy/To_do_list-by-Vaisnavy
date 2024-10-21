import random
import string

def generate_password(length):
    # Define the character set to use for password generation
    lower = string.ascii_lowercase  # a-z
    upper = string.ascii_uppercase  # A-Z
    digits = string.digits           # 0-9
    special = string.punctuation     # Special characters

    # Combine all characters into one string
    all_characters = lower + upper + digits + special

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate the password
    generated_password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
