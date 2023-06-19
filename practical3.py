#Practical-3
#Implement Playfair cipher encryption-decryption
def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")  # Replace J with I
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabet_set = set(alphabet)
    remaining_letters = "".join(alphabet_set - key_set)
    playfair_matrix = list(key) + list(remaining_letters)
    return playfair_matrix

def generate_playfair_pairs(text):
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            pairs.append(text[i] + "X")
            i += 1
        else:
            pairs.append(text[i] + text[i + 1])
            i += 2
    return pairs

def get_playfair_coordinates(playfair_matrix, letter):
    index = playfair_matrix.index(letter)
    row = index // 5
    col = index % 5
    return row, col

def playfair_encrypt(text, playfair_matrix):
    encrypted_text = ""
    pairs = generate_playfair_pairs(text.replace(" ", "").upper())
    for pair in pairs:
        a, b = pair[0], pair[1]
        row_a, col_a = get_playfair_coordinates(playfair_matrix, a)
        row_b, col_b = get_playfair_coordinates(playfair_matrix, b)

        if row_a == row_b:
            col_a = (col_a + 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5
            row_b = (row_b + 1) % 5
        else:
            col_a, col_b = col_b, col_a

        encrypted_text += playfair_matrix[row_a * 5 + col_a]
        encrypted_text += playfair_matrix[row_b * 5 + col_b]
    return encrypted_text

def playfair_decrypt(encrypted_text, playfair_matrix):
    decrypted_text = ""
    pairs = generate_playfair_pairs(encrypted_text.upper())
    for pair in pairs:
        a, b = pair[0], pair[1]
        row_a, col_a = get_playfair_coordinates(playfair_matrix, a)
        row_b, col_b = get_playfair_coordinates(playfair_matrix, b)

        if row_a == row_b:
            col_a = (col_a - 1) % 5
            col_b = (col_b - 1) % 5
        elif col_a == col_b:
            row_a = (row_a - 1) % 5
            row_b = (row_b - 1) % 5
        else:
            col_a, col_b = col_b, col_a

        decrypted_text += playfair_matrix[row_a * 5 + col_a]
        decrypted_text += playfair_matrix[row_b * 5 + col_b]
    return decrypted_text

# Generate Playfair matrix
key = "VIPULPATIlIS"
playfair_matrix = generate_playfair_matrix(key)
print("Playfair Matrix:")
for i in range(0, 25, 5):
    print(playfair_matrix[i:i+5])
print()

plaintext = "HELLO WORLD"

encrypted_text = playfair_encrypt(plaintext, playfair_matrix)
print("Encrypted text:", encrypted_text)

decrypted_text = playfair_decrypt(encrypted_text, playfair_matrix)
print("Decrypted text:", decrypted_text)


