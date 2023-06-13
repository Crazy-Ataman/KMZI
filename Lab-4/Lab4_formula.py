from matplotlib import pyplot as plt
import time

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ '

def encrypt(text):
    N = len(alphabet)  # number of characters in the alphabet
    k = 7              # shift key
    result = ''
    for char in text:
        if char.upper() in alphabet:
            x = alphabet.index(char.upper())
            y = (x + k) % N
            encrypted = alphabet[y]
        else:
            encrypted = char
        result += encrypted
    return result


def decrypt(text):
    N = len(alphabet)  # number of characters in the alphabet
    k = 7              # shift key
    result = ''
    for char in text:
        if char.upper() in alphabet:
            y = alphabet.index(char.upper())
            x = (y - k) % N
            decrypted = alphabet[x]
        else:
            decrypted = char
        result += decrypted
    return result

def BuildHistogram(alphabet, message, encrypted_message):
    list_alphabet = [i for i in alphabet]
    np_probability_original_message = [round(message.count(i) / len(message), 4) for i in alphabet]
    np_probability_encrypted_message = [round(encrypted_message.count(i) / len(encrypted_message), 4) for i in alphabet]

    fig, ax = plt.subplots(2, 1)
    ax[0].bar(list_alphabet, np_probability_original_message)
    ax[1].bar(list_alphabet, np_probability_encrypted_message)
    plt.show()


# read the input file
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

start_time = time.time()
# encrypt the text
encrypted_text = encrypt(text)
encryption_time = round(time.time() - start_time, 7)

# write the encrypted text to a file
with open('encrypted.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)

# read the encrypted file
with open('encrypted.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

start_time = time.time()
# decrypt the text
decrypted_text = decrypt(encrypted_text)
decryption_time = round(time.time() - start_time, 7)

# write the decrypted text to a file
with open('decrypted.txt', 'w', encoding='utf-8') as file:
    file.write(decrypted_text)

print("Encryption time: " + str(encryption_time) + " seconds")
print("Decryption time: " + str(decryption_time) + " seconds")

BuildHistogram(alphabet, text, encrypted_text)
