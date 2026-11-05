def combine_files(path):
    writeto = os.path.join(path, 'combined.txt')
    with open(writeto, 'w') as writing:
        for file in os.listdir(path):
            filepath = os.path.join(path,file)
            if os.path.isfile(filepath) and '.txt' in file and file !='combined.txt':
                with open(filepath, encoding='cp1252') as f:
                    content = f.read()
                    writing.write(content)
    with open(writeto, encoding='cp1252') as f:
        endproduct = f.read()
    return endproduct
 
import os


path = r'week_9\number_lines'
print(combine_files(path))