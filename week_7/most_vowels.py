example = 'Leif smells'
example2 = 'Leif smells really bad'
example3 = 'Leif smells extremely bad'
example4 = 'Eskild eats'

def most_vowels(sentence):
    vowels = 'aeiou'
    split_sentence = sentence.split()
    for word in split_sentence:
        vowel_counter = 0
        for character in word:
            if character in vowels:
                vowel_counter += 1
        print(vowel_counter,word)
    print(split_sentence)



most_vowels(example)
most_vowels(example2)
most_vowels(example3)
most_vowels(example4)