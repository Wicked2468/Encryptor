from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os

class Blowfish:
    @staticmethod
    def generate_key(password):
        """
        Generates a new Blowfish encryption key from the provided password.

        Args:
            password (str): The password to use for generating the key.

        Returns:
            bytes: The generated encryption key.
        """
        return os.urandom(16)  # 128-bit Blowfish key

    @staticmethod
    def encrypt_file(key, input_file_path):
        """
        Encrypts the contents of the input file using the Blowfish algorithm and saves the encrypted data to a new file.

        Args:
            key (bytes): The encryption key to use.
            input_file_path (str): The path of the file to be encrypted.

        Returns:
            None
        """
        with open(input_file_path, 'rb') as file:
            plaintext = file.read()

        cipher = Cipher(algorithms.Blowfish(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = PKCS7(algorithms.Blowfish.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()
        encrypted = encryptor.update(padded_plaintext) + encryptor.finalize()

        output_file_path = os.path.splitext(input_file_path)[0] + '.blowfish.enc'
        with open(output_file_path, 'wb') as file:
            file.write(encrypted)