import hashlib

def calcular_sha256(texto: str) -> str:
    """
    Calcula el hash SHA-256 de una cadena de texto.

    Args:
        texto (str): La cadena de texto de la que se desea calcular el hash.

    Returns:
        str: El hash SHA-256 de la cadena de texto.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(texto.encode('utf-8'))
    return sha256_hash.hexdigest()

# Ejemplo de uso
texto = "Hola, mundo!"
hash_resultado = calcular_sha256(texto)
print(f"El hash SHA-256 de '{texto}' es: {hash_resultado}")
