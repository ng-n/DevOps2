import string
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    # Ensure at least one character of each type
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    # Generate remaining characters
    remain_length = length - 4
    password.extend(random.choice(chars) for _ in range(remain_length))

    # Shuffle the password characters
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":

    print("Welcome to the Linux User Password Generator!")
    
    while True:
        try:
            length = int(input("\nPlease enter the desired password length: "))
            
            if length < 4:
                print("\nPassword length should be at least 4.")
            else:
                break       
        except ValueError:
            print("\nInvalid input. Please enter a valid integer for password length.")
    
    password = generate_password(length)
    print(f"\nGenerated password: {password}")