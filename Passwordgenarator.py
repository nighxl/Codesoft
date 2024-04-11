import random
import string

def generate_password(length):
    # Define the characters that will be used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired password length: "))

# Generate and display the password
generated_password = generate_password(password_length)
print("Generated password:", generated_password)
