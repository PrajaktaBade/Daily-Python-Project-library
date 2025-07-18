import random
import string

def generate_password(length,include_uppercase,include_numbers,include_specials):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    specials = string.punctuation if include_specials else ''
    
    all_chars = lowercase + uppercase + numbers + specials
    if not all_chars:
        raise ValueError("At least one character type must be selected.")   
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length (minimum 1): "))
        if length < 6:
            raise ValueError("Password length must be at least 1.")
        
        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, include_uppercase, include_numbers, include_specials)
        print(f"Generated password: {password}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


        
if __name__ == "__main__":
    main()
    print("Goodbye!")