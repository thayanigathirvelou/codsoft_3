import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("===== Password Generator =====")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a valid length.")

if __name__ == "__main__":
    main()
