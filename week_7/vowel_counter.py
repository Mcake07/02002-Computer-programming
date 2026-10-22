def vowel_counter(text):
    vowels = 'aeiou'
    amount = 0
    for word in text.split():
        for letter in word:
            if letter.lower() in vowels:
                amount += 1

    return amount

print(vowel_counter('test eeee ssss'))