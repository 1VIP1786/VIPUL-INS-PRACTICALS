#Practical-6
#Implement Simple Transposition encryption-decryption
def simple_transposition_encrypt(plaintext, key):
    key = [int(char) for char in key]
    num_columns = len(key)
    num_rows = -(-len(plaintext) // num_columns)  # Ceiling division
    plaintext += " " * (num_rows * num_columns - len(plaintext))  # Add padding if needed
    encrypted_text = ""
    for col in key:
        for row in range(num_rows):
            index = row * num_columns + col - 1
            encrypted_text += plaintext[index]
    return encrypted_text

def simple_transposition_decrypt(encrypted_text, key):
    key = [int(char) for char in key]
    num_columns = len(key)
    num_rows = -(-len(encrypted_text) // num_columns)  # Ceiling division
    decrypted_text = ""
    for row in range(num_rows):
        for col in key:
            index = row * num_columns + col - 1
            decrypted_text += encrypted_text[index]
    decrypted_text = decrypted_text.rstrip()  # Remove trailing padding
    return decrypted_text

# Test the Simple Transposition cipher
plaintext = "HELLO VIPUL"
key = "321"

encrypted_text = simple_transposition_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = simple_transposition_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
