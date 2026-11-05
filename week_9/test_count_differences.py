import os

filename1 = 'week_9/week_9_files/results_A1.txt'
if not os.path.isfile(filename1):
    print('Test for Count Differences failed because filename1 could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct folder in VSCode.')
    exit(1)

from week_9_files.count_differences import count_differences


filename2 = 'week_9/week_9_files/results_A2.txt'
returned = count_differences(filename1, filename2)
expected = 3

if returned != expected:
    print('Test for Count Differences failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for Count Differences passed')