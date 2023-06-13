from matplotlib import pyplot as plt
import time

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read().upper()

alphabet_de = u"ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"

def Trisemus(key_word, strvalue, action):
    keyword, (height, width) = key_word
    doEncode = True if action == "encd" else False
    doDecode = True if action == "decd" else False

    start_pos = 0
    table = [['.' for x in range(width)] for y in range(height)]
    temp_char = {}
    for i in keyword + alphabet_de:
        if temp_char.get(i) is None:
            temp_char[i] = start_pos
            table[int(start_pos / width)][int(start_pos % width)] = i
            start_pos += 1
            if start_pos >= width * height:
                break

    print(table)
    result = ""
    for i in strvalue:
        start_pos = temp_char.get(i)
        if start_pos is not None:
            x = start_pos % width
            if doEncode:
                y = (start_pos // width + 1) % height
            elif doDecode:
                y = (start_pos // width - 1 + height) % height
            else:
                y = start_pos // width % height
            result += table[int(y)][int(x)]
        else:
            result += i
    return result

def BuildHistogram(alphabet, message, encrypted_message):
    list_alphabet = [i for i in alphabet]
    np_probability_original_message = [round(message.count(i) / len(message), 4) for i in alphabet]
    np_probability_encrypted_message = [round(encrypted_message.count(i) / len(encrypted_message), 4) for i in alphabet]

    fig, ax = plt.subplots(2, 1)
    ax[0].bar(list_alphabet, np_probability_original_message)
    ax[1].bar(list_alphabet, np_probability_encrypted_message)
    plt.show()

keyword = 'ENIGMA'
tablesize = (5, 6)

key = (keyword, tablesize)
print("Key = " + str(key))

start_time = time.time()
encrypted_text = Trisemus(key, text, "encd")
encryption_time = round(time.time() - start_time, 7)
with open('encrypted_text.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted_text)

start_time = time.time()
decrypted_text = Trisemus(key, encrypted_text, "decd")
decryption_time = round(time.time() - start_time, 7)
with open('decrypted_text.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted_text)

print("Encryption time: " + str(encryption_time) + " seconds")
print("Decryption time: " + str(decryption_time) + " seconds")

BuildHistogram(alphabet_de, text, encrypted_text)