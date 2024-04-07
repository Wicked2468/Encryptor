from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os

class DES:
    @staticmethod
    def generate_key(password):
        """
        Generates a new DES encryption key from the provided password.

        Args:
            password (str): The password to use for generating the key.

        Returns:
            bytes: The generated encryption key.
        """
        return os.urandom(8)  # 64-bit DES key

    @staticmethod
    def encrypt_file(key, input_file_path):
        """
        Encrypts the contents of the input file using the DES algorithm and saves the encrypted data to a new file.

        Args:
            key (bytes): The encryption key to use.
            input_file_path (str): The path of the file to be encrypted.

        Returns:
            None
        """
        with open(input_file_path, 'rb') as file:
            plaintext = file.read()

        cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = PKCS7(algorithms.TripleDES.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()
        encrypted = encryptor.update(padded_plaintext) + encryptor.finalize()

        output_file_path = os.path.splitext(input_file_path)[0] + '.des.enc'
        with open(output_file_path, 'wb') as file:
            file.write(encrypted)