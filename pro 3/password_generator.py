import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for complexity.")
        return None

    # Define character pools
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    specials = string.punctuation   # special chars like !@#$%

    # Ensure password contains at least one character from each category
    password_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(specials)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = letters + digits + specials
    password_chars += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)

    # Join to form the final password string
    return ''.join(password_chars)

def main():
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()
