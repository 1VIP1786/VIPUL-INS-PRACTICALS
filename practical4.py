#Practical-4
#Implement Polyalphabetic cipher encryption-decryption
def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    plaintext = plaintext.upper()
    key = key.upper()
    key_length = len(key)
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Test the Vigenère cipher
plaintext = "VIPUL PATIL"
key = "KEY"
print("Plain text:",plaintext)
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
