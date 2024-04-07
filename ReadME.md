# Encryption Algorithms

This Python script provides functionality to encrypt and decrypt files using different encryption algorithms such as Fernet, AES, DES, and Blowfish. It allows users to select an encryption algorithm, provide a password to generate an encryption key, and then encrypt or decrypt files accordingly.

## Usage

1. **Encryption:**

    To encrypt a file, run the script and choose the `encrypt` operation. Then follow these steps:
    
    - Choose an encryption algorithm (`fernet`, `aes`, `des`, `blowfish`).
    - Enter a password.
    - Provide the path of the file to be encrypted.

2. **Decryption:**

    To decrypt a file, run the script and choose the `decrypt` operation. Then follow these steps:
    
    - Choose the encryption algorithm that was used for encryption (`fernet`, `aes`, `des`, `blowfish`).
    - Enter the encryption key (for Fernet, use the generated key directly; for other algorithms, use the password that was used for encryption).
    - Provide the path of the encrypted file.

## Supported Encryption Algorithms

- **Fernet**: A symmetric encryption algorithm.
- **AES (Advanced Encryption Standard)**: A symmetric encryption algorithm with support for different key sizes.
- **DES (Data Encryption Standard)**: An older symmetric encryption algorithm, less secure compared to AES.
- **Blowfish**: A symmetric encryption algorithm with variable key length support.

## File Structure

The script consists of the following components:

- **Main Functions**: `generate_key`, `encrypt_file`, and `decrypt_file` are responsible for key generation, file encryption, and file decryption, respectively.
- **Encryption Algorithm Implementations**: The script imports and utilizes implementations of encryption algorithms (`Fernet`, `AES`, `DES`, `Blowfish`) from separate modules (`encryption_algorithms`).
- **User Interface**: The `main` function provides a command-line interface for users to interact with the script.

## Note

- Ensure that the required dependencies (`cryptography`) are installed before running the script.
- Always remember to securely manage encryption keys and passwords.
- Use appropriate encryption algorithms and key sizes based on security requirements.
- This script currently supports only file-based encryption and decryption. Additional features such as folder encryption may be added in future updates.
- Still Working on the decryption part

