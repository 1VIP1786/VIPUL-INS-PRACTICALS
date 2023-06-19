#Practical-8
#Implement Diffi-Hellmen Key exchange Method
def calculate_shared_key(base, prime, private_key):
    shared_key = pow(base, private_key, prime)
    return shared_key

# Step 1: Agree on a prime number and base
prime = 23
base = 5

# Step 2: Each party generates a private key
private_key_A = 6
private_key_B = 15

# Step 3: Calculate the shared keys
shared_key_A = calculate_shared_key(base, prime, private_key_A)
shared_key_B = calculate_shared_key(base, prime, private_key_B)

# Step 4: Exchange the shared keys

# Step 5: Calculate the final secret keys
final_secret_key_A = calculate_shared_key(shared_key_B, prime, private_key_A)
final_secret_key_B = calculate_shared_key(shared_key_A, prime, private_key_B)

# Step 6: Verify that the final secret keys match
if final_secret_key_A == final_secret_key_B:
    print("Final secret keys match:", final_secret_key_A)
else:
    print("Final secret keys do not match")
