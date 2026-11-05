import os

def number_lines(filename):
    with open(filename, encoding='cp1252') as f:
        content = f.read()
    lines = content.splitlines()
    no_Title = lines[1:]
    title = lines[0]
    lyrics = []
    song = []
    song.append(title)
    for line in no_Title:
        if line != '':
            lyrics.append(line)
    for i in range(len(lyrics)):
        line = f'{i:02d}  {lyrics[i]}'
        song.append(line)
    head, tail = os.path.split(filename)
    tail = tail.replace('.txt','')
    tail += '_numbered.txt'
    new_fileName = os.path.join(head,tail)
    with open(new_fileName, 'w') as f:
        for i in range(len(song)):
            f.write(str(song[i]) + '\n')
    with open(new_fileName) as f:
        content = f.read()
    return content

def join(head,tail):
    return os.path.join(head,tail)

path = r'week_9\number_lines'
file = 'bro_bro_brille.txt'

print(number_lines(join(path,file)))

file = 'combined.txt'

print(number_lines(join(path,file)))

file = 'der_bor_en_bager.txt'

print(number_lines(join(path,file)))

file = 'fastelavn_er_mit_navn.txt'

print(number_lines(join(path,file)))

file = 'se_den_lille_kattekilling.txt'

print(number_lines(join(path,file)))