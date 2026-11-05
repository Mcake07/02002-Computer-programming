def letter_counter(filename):
    alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
    count = {}
    for letter in alphabet:
        count[letter] = 0
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    words = content.split(' ')
    for word in words:
        for letter_w in word:
            for letter_a in alphabet:
                if letter_a == letter_w:
                    count[letter_a] += 1
    return count

import os

for file in os.listdir(r'week_9\texts'):
    if os.path.isfile(os.path.join(r'week_9\texts', file)):
        print(letter_counter(os.path.join(r'week_9\texts',file)), '\n\n\n')