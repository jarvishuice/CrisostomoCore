import hashlib
class Cipher:
    def __init__(self):
        pass
    def encrypt(self, text: str) -> str:
        """
            Calcula el hash SHA-256 de una cadena de texto.

            Args:
                text (str): La cadena de texto de la que se desea calcular el hash.

            Returns:
                str: El hash SHA-256 de la cadena de texto.
        """
        sha256_hash = hashlib.sha256()
        sha256_hash.update(text.encode('utf-8'))
        return sha256_hash.hexdigest()


       
