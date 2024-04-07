from encryption_algorithms.fernet import Fernet
from encryption_algorithms.aes import AES
from encryption_algorithms.des import DES
from encryption_algorithms.blowfish import Blowfish

def generate_key(password, algorithm):
    """
    Generates a new encryption key based on the selected algorithm.

    Args:
        password (str): The password to use for generating the key.
        algorithm (str): The encryption algorithm to use ('fernet', 'aes', 'des', 'blowfish').

    Returns:
        bytes: The generated encryption key.
    """
    if algorithm == 'fernet':
        return Fernet.generate_key()
    elif algorithm == 'aes':
        return AES.generate_key(password)
    elif algorithm == 'des':
        return DES.generate_key(password)
    elif algorithm == 'blowfish':
        return Blowfish.generate_key(password)
    else:
        raise ValueError("Invalid encryption algorithm selected.")

def encrypt_file(key, input_file_path, algorithm):
    """
    Encrypts the contents of the input file and saves the encrypted data to a new file.

    Args:
        key (bytes): The encryption key to use.
        input_file_path (str): The path of the file to be encrypted.
        algorithm (str): The encryption algorithm to use ('fernet', 'aes', 'des', 'blowfish').

    Returns:
        None
    """
    if algorithm == 'fernet':
        Fernet.encrypt_file(key, input_file_path)
    elif algorithm == 'aes':
        AES.encrypt_file(key, input_file_path)
    elif algorithm == 'des':
        DES.encrypt_file(key, input_file_path)
    elif algorithm == 'blowfish':
        Blowfish.encrypt_file(key, input_file_path)
    else:
        raise ValueError("Invalid encryption algorithm selected.")

def decrypt_file(key, input_file_path, algorithm):
    """
    Decrypts the contents of the encrypted file and saves the decrypted data to a new file.

    Args:
        key (bytes): The encryption key to use.
        input_file_path (str): The path of the encrypted file to be decrypted.
        algorithm (str): The encryption algorithm to use ('fernet', 'aes', 'des', 'blowfish').

    Returns:
        None
    """
    if algorithm == 'fernet':
        Fernet.decrypt_file(key, input_file_path)
    elif algorithm == 'aes':
        AES.decrypt_file(key, input_file_path)
    elif algorithm == 'des':
        DES.decrypt_file(key, input_file_path)
    elif algorithm == 'blowfish':
        Blowfish.decrypt_file(key, input_file_path)
    else:
        raise ValueError("Invalid encryption algorithm selected.")

def main():
    operation = input("Enter 'encrypt' to encrypt a file or 'decrypt' to decrypt a file: ")

    if operation.lower() == 'encrypt':
        algorithm = input("Choose an encryption algorithm (fernet, aes, des, blowfish): ")
        password = input("Enter the password: ")
        key = generate_key(password, algorithm)

        input_file_path = input("Enter the path of the file you want to encrypt: ")
        encrypt_file(key, input_file_path, algorithm)
        #Still working on Decryption part :)
    elif operation.lower() == 'decrypt':
        algorithm = input("Choose the encryption algorithm (fernet, aes, des, blowfish): ")
        key_str = input("Enter the encryption key: ")
        key = key_str.encode()  # Convert string to bytes

        input_file_path = input("Enter the path of the encrypted file you want to decrypt: ")
        decrypt_file(key, input_file_path, algorithm)
    else:
        print("Invalid operation. Please try again.")

if __name__ == "__main__":
    main()