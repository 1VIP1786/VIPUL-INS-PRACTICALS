#Practical-7
#Implement One time pad encryption-decryption
def one_time_pad_encrypt(plaintext, key):
    # Convert plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()

    # Ensure that the key is at least as long as the plaintext
    if len(key) < len(plaintext):
        raise ValueError("Key length should be at least equal to plaintext length.")

    encrypted_text = ""
    for i in range(len(plaintext)):
        # Get the ASCII values of the plaintext and key characters
        plaintext_ascii = ord(plaintext[i]) - ord('A')
        key_ascii = ord(key[i]) - ord('A')

        # Apply modular addition to perform the encryption
        encrypted_ascii = (plaintext_ascii + key_ascii) % 26

        # Convert the encrypted ASCII value back to a character and append it to the result
        encrypted_char = chr(encrypted_ascii + ord('A'))
        encrypted_text += encrypted_char

    return encrypted_text


def one_time_pad_decrypt(encrypted_text, key):
    # Convert encrypted text and key to uppercase
    encrypted_text = encrypted_text.upper()
    key = key.upper()

    # Ensure that the key is at least as long as the encrypted text
    if len(key) < len(encrypted_text):
        raise ValueError("Key length should be at least equal to encrypted text length.")

    decrypted_text = ""
    for i in range(len(encrypted_text)):
        # Get the ASCII values of the encrypted text and key characters
        encrypted_ascii = ord(encrypted_text[i]) - ord('A')
        key_ascii = ord(key[i]) - ord('A')

        # Apply modular subtraction to perform the decryption
        decrypted_ascii = (encrypted_ascii - key_ascii) % 26

        # Convert the decrypted ASCII value back to a character and append it to the result
        decrypted_char = chr(decrypted_ascii + ord('A'))
        decrypted_text += decrypted_char

    return decrypted_text


# Test the One-Time Pad cipher
plaintext = "VIPUL PATIL"  # The plaintext to be encrypted
key = "KEYKEYKEYKEYKEY"  # The key for encryption, repeated to match the length of the plaintext

encrypted_text = one_time_pad_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = one_time_pad_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

