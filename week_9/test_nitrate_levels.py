import os

path = 'week_9/week_9_files/nitrate_data_A.txt'
if not os.path.isfile(path):
    print('Test for Nitrate Levels failed because path could not be found.')
    print('This does not indicate anything about the correctness of your code.')
    print('Please open the correct folder in VSCode.')
    exit(1)

from week_9_files.nitrate_levels import nitrate_levels


returned = nitrate_levels(path)
expected = (0, 0, 8, 2, 0)

if returned != expected:
    print('Test for Nitrate Levels failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for Nitrate Levels passed')