from normal_range import normal_range

returned = normal_range(1.73)
expected = 'Normal weight range: 56 to 74 kg'

if returned != expected:
    print('Test for Normal Range failed because returned was:')
    print(repr(returned))
    print('instead of:')
    print(repr(expected))
else:
    print('Test for Normal Range passed')