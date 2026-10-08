def stable_measurements(measurements):
    stable = []
    for i in range(1,len(measurements)-1):
        before = measurements[:i]
        after = measurements[i+1:len(measurements)]
        if measurements[i] > max(before) and measurements[i] < min(after):
            return measurements[i:]

    return []


print(stable_measurements([1.8,1.9,0.3,0.2,1.1,2.8,5.0,9.5,22.5]))
print(stable_measurements([1.9,0.3,0.7,2.0,0.6,0.9,3.1,3.7,8.4]))