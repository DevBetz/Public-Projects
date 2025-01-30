import random
import string

def generate_password(length, use_special, use_numbers, use_uppercase):
    characters = string.ascii_lowercase
    if use_special:
        characters += '!@#$%^&*()_+,.<>?/-=~|'
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    
    if not characters:
        print("You must select at least one type of character.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("How many characters do you want the password to be? "))
    use_special = input("Do you want to use special characters? (yes/no): ").lower() == "yes"
#    how_many_special = int(input(f"How many Special Characters do you want to use?\n"))
    use_numbers = input("Use numbers as well? (yes/no): ").lower() == "yes"
#    how_many_numbers = int(input(f"How many Numbers do you want to use?\n"))
    use_uppercase = input("Do you want to use uppercase letters? (yes/no): ").lower() == "yes"
#    how_many_uppercase = int(input(f"How many Uppercase Characters do you want to use?\n"))

#want to add quantity of special, number, and capital characters.

    password = generate_password(length, use_special, use_numbers, use_uppercase)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
