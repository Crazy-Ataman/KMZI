import numpy as np
import time
from matplotlib import pyplot as plt

# Define the keys as name and surname
name = "Maksim"
surname = "Dashchinskii"

alphabet_de = u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define the encryption function using a stream cipher
def encrypt(plaintext, key_matrix):
    ciphertext = ""
    prev_char = "A"
    for i in range(len(plaintext)):
        j = i % key_matrix.shape[1]
        k = (i // key_matrix.shape[1]) % key_matrix.shape[0]
        row = (ord(prev_char) + key_matrix[k][j]) % 26
        col = j
        curr_char = chr((ord(plaintext[i]) - ord("A") + key_matrix[k][j]) % 26 + ord("A"))
        ciphertext += curr_char
        prev_char = curr_char
    return ciphertext

# Define the decryption function using the same key matrix as the encryption function
def decrypt(ciphertext, key_matrix):
    plaintext = ""
    prev_char = "A"
    for i in range(len(ciphertext)):
        j = i % key_matrix.shape[1]
        k = (i // key_matrix.shape[1]) % key_matrix.shape[0]
        row = (ord(prev_char) + key_matrix[k][j]) % 26
        col = j
        curr_char = chr((ord(ciphertext[i]) - ord("A") - key_matrix[k][j]) % 26 + ord("A"))
        plaintext += curr_char
        prev_char = ciphertext[i]
    return plaintext

def BuildHistogram(alphabet, message, encrypted_message):
    list_alphabet = [i for i in alphabet]
    np_probability_original_message = [round(message.count(i) / len(message), 4) for i in alphabet]
    np_probability_encrypted_message = [round(encrypted_message.count(i) / len(encrypted_message), 4) for i in alphabet]

    fig, ax = plt.subplots(2, 1)
    ax[0].bar(list_alphabet, np_probability_original_message)
    ax[1].bar(list_alphabet, np_probability_encrypted_message)
    plt.show()

# Read the plaintext from a file
with open("text.txt", "r", encoding="utf-8") as f:
    plaintext = f.read().upper()

# Remove any whitespace and special characters from the plaintext
plaintext = "".join(c for c in plaintext if c.isalpha())

# Generate the key matrix using the keys
num_rows = len(surname)
num_cols = len(name)
key_matrix = np.zeros((num_rows, num_cols), dtype=int)
for i in range(num_rows):
    for j in range(num_cols):
        key_matrix[i][j] = ord(surname[i]) + ord(name[j])

start_time = time.time()
# Encrypt the plaintext using the stream cipher
ciphertext = encrypt(plaintext, key_matrix)
encryption_time = round(time.time() - start_time, 7)

start_time = time.time()
# Decrypt the ciphertext using the same key matrix as the encryption function
decrypted_plaintext = decrypt(ciphertext, key_matrix)
decryption_time = round(time.time() - start_time, 7)

# Print the original plaintext, encrypted ciphertext, and decrypted plaintext
print("Original plaintext: " + plaintext)
print("Encrypted ciphertext: " + ciphertext)
print("Decrypted plaintext: " + decrypted_plaintext)
print("Encryption time: " + str(encryption_time) + " seconds")
print("Decryption time: " + str(decryption_time) + " seconds")

BuildHistogram(alphabet_de, plaintext, ciphertext)