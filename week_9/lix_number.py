def lix_number(filename):
    dotComma = '.,'
    long_words = 0
    dots = 0
    noDotCommaWord = None
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    words = content.split()
    words_amount = len(words)
    for i in range(len(words)):
        word = words[i]
        noDotCommaWord = word.replace(',','').replace('.','')
        word_length = len(noDotCommaWord)
        dots += word.count('.')
        if word_length > 6: 
            long_words += 1
    LIX = (words_amount / dots) + (long_words * 100 / words_amount)
    return LIX

def join(path,file):
    import os
    return os.path.join(path,file)

path = r'week_9\texts'
file = 'text_lix_a.txt'

print(lix_number(join(path,file)))

file = 'text_lix_g.txt'

print(lix_number(join(path,file)))