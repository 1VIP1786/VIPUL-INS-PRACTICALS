#Practical-2
#Implement Monoalphabetic cipher encryption-decryption

import random

def generate_substitution_key():
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabets)
    substitution_key = "".join(alphabets)
    return substitution_key

def monoalphabetic_encrypt(text, substitution_key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = substitution_key[ord(char.lower()) - ord('a')].upper()
            else:
                encrypted_char = substitution_key[ord(char) - ord('a')]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def monoalphabetic_decrypt(encrypted_text, substitution_key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(ord('A') + substitution_key.index(char.lower()))
            else:
                decrypted_char = chr(ord('a') + substitution_key.index(char))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Generate substitution key
substitution_key = generate_substitution_key()
print("Substitution Key:", substitution_key)

plaintext = "Hello, World!"

encrypted_text = monoalphabetic_encrypt(plaintext, substitution_key)
print("Encrypted text:", encrypted_text)

decrypted_text = monoalphabetic_decrypt(encrypted_text, substitution_key)
print("Decrypted text:", decrypted_text)


