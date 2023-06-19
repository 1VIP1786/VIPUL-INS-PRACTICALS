#Practical-9
#Implement RSA encryption-decryption algorithm
import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime():
    while True:
        prime_candidate = random.randint(2**15, 2**16)
        if is_prime(prime_candidate):
            return prime_candidate

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    _, x, _ = extended_gcd(e, phi)
    return x % phi

def generate_keys():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = multiplicative_inverse(e, phi)

    return (e, n), (d, n)

def rsa_encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def rsa_decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)


# Generate RSA keys
public_key, private_key = generate_keys()
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Encrypt a message
message = "HELLO WORLD"
encrypted_message = rsa_encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

# Decrypt the encrypted message
decrypted_message = rsa_decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
