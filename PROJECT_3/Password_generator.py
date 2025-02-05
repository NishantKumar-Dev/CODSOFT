import random
import string

def generate_password(length, complexity):
    if complexity == 'easy':
        characters = string.ascii_letters + string.digits
    elif complexity == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'very strong':
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    else:
        raise ValueError("Invalid complexity option")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))

print("Choose the complexity of the password:")
print("1. Easy (Letters and digits only)")
print("2. Hard (Letters, digits, and punctuation)")
print("3. Very Strong (Letters, digits, punctuation, and spaces)")

complexity = input("Enter 'easy', 'hard', or 'very strong': ").lower()

password = generate_password(length, complexity)
print("Generated Password:", password)
