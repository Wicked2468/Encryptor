# File Encryption with Fernet

This Python script provides a simple way to encrypt files using the Fernet symmetric encryption algorithm provided by the `cryptography` library. Fernet ensures secure encryption and decryption of data.

## How to Use

1. **Installation**: Ensure you have Python installed on your system. If not, you can download and install it from [python.org](https://www.python.org/downloads/). Additionally, install the `cryptography` library by running:

2. **Running the Script**: Execute the script by running the command:

3. **Enter Password**: Upon running the script, you will be prompted to enter a password. This password is used to generate an encryption key. Ensure you remember this password as it will be required for decryption.

4. **Enter File Path**: Enter the path of the file you wish to encrypt when prompted. The script will encrypt the file using the generated key.

5. **Encryption Process**: The script encrypts the specified file and saves the encrypted data to a new file with the `.enc` extension appended to the original file name. Additionally, it prints the path of the encrypted file and the encryption key used. 

## Important Notes

- Ensure you keep the password used to encrypt the file safe and secure. Without this password, decryption of the file will not be possible.
- This script utilizes symmetric encryption, meaning the same key is used for both encryption and decryption.
- The `cryptography` library provides strong encryption algorithms, ensuring the security of your data.

## Disclaimer

- This script is provided as-is and should be used for educational or personal purposes only. It is not intended for use in a production environment without proper testing and validation.
- Always ensure you have the necessary permissions to access and modify the files you are encrypting.
- Use caution when handling sensitive data and ensure compliance with applicable laws and regulations regarding data privacy and security.
