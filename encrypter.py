from cryptography.fernet import Fernet

def generate_key(password):
    return Fernet.generate_key()

def encrypt_file(key, input_file_path):
    f = Fernet(key)
    try:
        with open(input_file_path, 'rb') as original_file:
            original = original_file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    encrypted = f.encrypt(original)
    output_file_path = input_file_path + '.enc'
    with open(output_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print("Encryption completed. Encrypted file saved as:", output_file_path)
    print("Encryption key:", key.decode())  # Convert bytes to string and print

def main():
    password = input("Enter the password: ")
    key = generate_key(password)

    input_file_path = input("Enter the path of the file you want to encrypt: ")

    encrypt_file(key, input_file_path)

if __name__ == "__main__":
    main()
