from simple_statistics import SimpleStatistics

import math

all_tests = []
samples = [ 0.67549219,  2.22054664,  0.4485289 , -1.07022885, -0.82199812,
        2.0338676 ,  1.18551193, -1.41304894, -0.02790234, -1.4454587 ,
       -0.54574887,  0.24266892,  1.48529121,  1.54283154,  0.10182828]

stat = SimpleStatistics(samples)
output = stat.get_mean()
expected = 0.3074787589954987
test = math.isclose(output, expected, rel_tol=0.001)
all_tests.append(test)
if not test:
    print("Test failed")
    print("samples =", samples)
    print("statistic = SimpleStatistics(samples) \nstatistic.get_mean() returned", output, 'Should return', expected)
else:
    print("Test passed")

print("##################################################################################################")
print("##################################################################################################")

output = stat.get_standard_deviation()
expected = 1.2122
test = math.isclose(output, expected, rel_tol=0.001)
all_tests.append(test)
if not test:
    print("Test failed")
    print("samples =", samples)
    print("statistic = SimpleStatistics(samples) \nstatistic.get_standard_deviation() returned", output, 'Should return', expected)
else:
    print("Test passed")

print("##################################################################################################")
print("##################################################################################################")


samples = [0.1763, -1.2523, 0.9099, -0.0679, 0.1999, 0.1175, 0.143, 0.1118, 0.9854, -1.1836, -0.5868, 0.4839, 1.2069, 0.142, 0.2523]

stat = SimpleStatistics(samples)
mu_zero = 0
output = stat.one_sample_ttest(mu_zero)
expected = False
test = output == expected
all_tests.append(test)
if not test:
    print("Test failed")
    print("samples =", samples)
    print(f"statistic = SimpleStatistics(samples) \nstatistic.one_sample_ttest({0}) returned", output, 'Should return', expected)
else:
    print("Test passed")

print("##################################################################################################")
print("##################################################################################################")

samples = [0.1763, -1.2523, 0.9099, -0.0679, 0.1999, 0.1175, 0.143, 0.1118, 0.9854, -1.1836, -0.5868, 0.4839, 1.2069, 0.142, 0.2523]

stat = SimpleStatistics(samples)
mu_zero = 1
output = stat.one_sample_ttest(mu_zero)
expected = True
test = output == expected
all_tests.append(test)
if not test:
    print("Test failed")
    print("samples =", samples)
    print(f"statistic = SimpleStatistics(samples) \nstatistic.one_sample_ttest({1}) returned", output, 'Should return', expected)
else:
    print("Test passed")

print("##################################################################################################")

print(f"You passed {sum(all_tests)}/{len(all_tests)} tests!")