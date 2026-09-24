height = 10
space = ' '
fill = '*'

for i in range(height):
    empty = height - i
    full = 1 + i * 2
    pattern = empty * space +  fill * full + empty * space
    print(pattern)