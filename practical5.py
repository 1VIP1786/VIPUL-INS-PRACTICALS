#Practical-5
#Implement Hill cipher encryption-decryption
import numpy as np

def hill_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    key_size = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape((key_size, key_size))
    plaintext_size = len(plaintext)
    padding_size = key_size - (plaintext_size % key_size)
    plaintext += "X" * padding_size  # Add padding if needed
    encrypted_text = ""
    for i in range(0, len(plaintext), key_size):
        block = np.array([ord(char) - ord('A') for char in plaintext[i:i+key_size]])
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_text += "".join([chr(char + ord('A')) for char in encrypted_block])
    return encrypted_text

def hill_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.replace(" ", "").upper()
    key = key.upper()
    key_size = int(np.sqrt(len(key)))
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape((key_size, key_size))
    key_inverse = np.linalg.inv(key_matrix)
    key_inverse = key_inverse.round()  # Round the elements to integers
    key_inverse = np.remainder(key_inverse, 26)  # Take modulo 26 of the elements
    key_inverse = key_inverse.astype(int)  # Convert the elements to integers
    decrypted_text = ""
    for i in range(0, len(encrypted_text), key_size):
        block = np.array([ord(char) - ord('A') for char in encrypted_text[i:i+key_size]])
        decrypted_block = np.dot(key_inverse, block) % 26
        decrypted_text += "".join([chr(char + ord('A')) for char in decrypted_block])
    return decrypted_text

# Test the Hill cipher
plaintext = "VIPUL PATIL"
key = "GYBNQKURP"
print("Plain text:",plaintext )
encrypted_text = hill_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = hill_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
