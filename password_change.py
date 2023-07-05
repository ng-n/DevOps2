import subprocess
import string
import random
import getpass

def get_existing_users():
    try:
        output = subprocess.check_output(['getent', 'passwd']).decode('utf-8')
        users = [line.split(':')[0] for line in output.split('\n') if line]
        return users
    except subprocess.CalledProcessError as e:
        print(f"Failed to get existing users: {str(e)}")
        return []

existing_users = get_existing_users()

def check_user_exists(username):
    if username in existing_users:
        return True
    return False

def generate_new_password():
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_requirements(password):
    min_length = 8

    if len(password) < min_length:
        return False
    
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return False

    return True
    

def change_password(username, password):
    try:
        command = f'echo "{username}:{password}" | sudo chpasswd'
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to change the password: {str(e)}")
        return False
    
if __name__ == "__main__":

    username = input("Enter username: ")

    if not check_user_exists(username):
        print("User does not exist.")
    else:
        password = getpass.getpass("Enter password (leave blank to generate a new password):")
        if not password:
            password = generate_new_password()
            print(f"Generated password: {password}")
            
        if not check_password_requirements(password):
            print("Password does not meet the requirements.")
            
        if password:
            if change_password(username, password):
                print("Password changed successfully.")
                print(f"Username: {username}")
                print(f"New password: {password}")
                print("Password meets the requirements.")
            else:
                print("Failed to change the password.")
        else:
            print("No password change required.")
