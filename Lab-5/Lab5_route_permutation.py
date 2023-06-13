import math
import time
from matplotlib import pyplot as plt

alphabet_de = u"abcdefghijklmnopqrstuvwxyz"

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

def enc(text):
    if math.sqrt(len(text)) <= 5:
        n = 5
    else: 
        n = math.ceil(math.sqrt(len(text)))

    a = ['_'] * n
    for i in range(n):
        a[i] = ['_'] * n

    text = text.replace(' ', '_')
    t = 0

    for i in range(0, n):
        for j in range(n * (i % 2) - i % 2,  n * ((i + 1) % 2)  - i % 2, 1 - (i % 2) * 2):
            if t < len(text):
                a[j][i] = text[t]
                t += 1
    
    enctext = ''

    for i in range(n):
        for j in range(n):
            enctext += a[i][j]
    return enctext

def dec(text):
    if math.sqrt(len(text)) <= 5:
        n = 5
    else: 
        n = math.ceil(math.sqrt(len(text)))

    a = ['_'] * n
    for i in range(n):
        a[i] = ['_'] * n

    t = 0

    for i in range(n):
        for j in range(n):
            if t < len(text):
                a[i][j] = text[t]
                t += 1
    
    dectext = ''

    for i in range(0, n):
        for j in range(n * (i % 2) - i % 2,  n * ((i + 1) % 2)  - i % 2, 1 - (i % 2) * 2):
            dectext += a[j][i]
    dectext = dectext.replace('_', ' ').strip()
    return dectext

def BuildHistogram(alphabet, message, encrypted_message):
    list_alphabet = [i for i in alphabet]
    np_probability_original_message = [round(message.count(i) / len(message), 4) for i in alphabet]
    np_probability_encrypted_message = [round(encrypted_message.count(i) / len(encrypted_message), 4) for i in alphabet]

    fig, ax = plt.subplots(2, 1)
    ax[0].bar(list_alphabet, np_probability_original_message)
    ax[1].bar(list_alphabet, np_probability_encrypted_message)
    plt.show()

start_time = time.time()
print("Cipher text: " + enc(text))
encryption_time = round(time.time() - start_time, 7)
print("-----------------------------")
start_time = time.time()
print("Deciphered text: " + dec(enc(text)))
decryption_time = round(time.time() - start_time, 7)
print("Encryption time: " + str(encryption_time) + " seconds")
print("Decryption time: " + str(decryption_time) + " seconds")

BuildHistogram(alphabet_de, text, enc(text))