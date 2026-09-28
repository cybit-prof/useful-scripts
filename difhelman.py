# Diffie-Hellman Key Exchange Demonstration with user input and math shown
print("Diffie-Hellman Key Exchange")

# Names of the two parties
name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")

# Public parameters
p = int(input("Enter the prime number (p): "))
g = int(input("Enter the generator (g): "))

# Private keys
private1 = int(input(f"Enter {name1}'s private key: "))
private2 = int(input(f"Enter {name2}'s private key: "))

# Calculate public keys
# Person 1: A = g^a mod p
public1 = pow(g, private1, p)

# Person 2: B = g^b mod p
public2 = pow(g, private2, p)

print("\n--- Public Keys ---")
# Show the math
print(f"{name1}: A = g^a mod p = {g}^{private1} mod {p}")
print(f"       {g}^{private1} = {g**private1}")
print(f"       {g**private1} mod {p} = {public1}")
print()
print(f"{name2}: B = g^b mod p = {g}^{private2} mod {p}")
print(f"       {g}^{private2} = {g**private2}")
print(f"       {g**private2} mod {p} = {public2}")
print()
print(f"{name1}'s public key:", public1)
print(f"{name2}'s public key:", public2)

# Calculate shared secret
# Person 1 computes B^a mod p
secret1 = pow(public2, private1, p)

# Person 2 computes A^b mod p
secret2 = pow(public1, private2, p)

print("\n--- Shared Secret ---")
# Show the math
print(f"{name1}: s = B^a mod p = {public2}^{private1} mod {p}")
print(f"       {public2}^{private1} = {public2**private1}")
print(f"       {public2**private1} mod {p} = {secret1}")
print()
print(f"{name2}: s = A^b mod p = {public1}^{private2} mod {p}")
print(f"       {public1}^{private2} = {public1**private2}")
print(f"       {public1**private2} mod {p} = {secret2}")
print()
print(f"Secret calculated by {name1}:", secret1)
print(f"Secret calculated by {name2}:", secret2)

if secret1 == secret2:
    print("\nSuccess!")
    print("Shared secret key =", secret1)
else:
    print("\nError: The shared secrets do not match.")
