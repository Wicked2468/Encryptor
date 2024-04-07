from cryptography.fernet import Fernet

class Fernet:
    @staticmethod
    def generate_key(password):
        """
        Generates a new Fernet encryption key from the provided password.

        Args:
            password (str): The password to use for generating the key.

        Returns:
            bytes: The generated encryption key.
        """
        return Fernet.generate_key()

    @staticmethod
    def encrypt_file(key, input_file_path):
        """
        Encrypts the contents of the input file using the Fernet algorithm and saves the encrypted data to a new file.

        Args:
            key (bytes): The encryption key to use.
            input_file_path (str): The path of the file to be encrypted.

        Returns:
            None
        """
        # Implementation omitted for brevity
        pass

    @staticmethod
    def decrypt_file(key, input_file_path):
        """
        Decrypts the contents of the encrypted file using the Fernet algorithm and saves the decrypted data to a new file.

        Args:
            key (bytes): The encryption key to use.
            input_file_path (str): The path of the encrypted file to be decrypted.

        Returns:
            None
        """
        # Implementation omitted for brevity
        pass