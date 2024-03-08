from cryptography.fernet import Fernet

def generate_key(password):
    return Fernet.generate_key()

def decrypt_file(key, input_file_path):
    f = Fernet(key)
    try:
        with open(input_file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
    except FileNotFoundError:
        print("Error: Encrypted file not found.")
        return

    decrypted = f.decrypt(encrypted)
    output_file_path = input_file_path[:-4]  # Remove '.enc' extension
    with open(output_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print("Decryption completed. Decrypted file saved as:", output_file_path)

def main():
    password = input("Enter the password: ")
    key = generate_key(password) # This key will be same as encryption key if generated with same password

    input_file_path = input("Enter the path of the file you want to decrypt: ")

    decrypt_file(key, input_file_path)

if __name__ == "__main__":
    main()
