from lucas_number import lucas_number

returned = lucas_number(3)
expected = 4

if returned != expected:
    print('Test for Lucas Number failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for Lucas Number passed')