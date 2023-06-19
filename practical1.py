#Practical-1
#Implement Caesar cipher encryption-decryption

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if not char.isalpha():
            decrypted_text += char
            continue

        ascii_offset = 65 if char.isupper() else 97
        decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        decrypted_text += decrypted_char

    return decrypted_text


plaintext = "Hello, VIPUL!"
shift = 3

encrypted_text = caesar_encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
