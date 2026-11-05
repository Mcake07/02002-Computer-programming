def nitrate_levels(filename):
    with open(filename) as f:
        content = f.read()
    data = content.split()
    very_low, low, normal, high, very_high = 0,0,0,0,0
    for i in range(len(data)):
        if float(data[i]) >= 50.0:
            very_high += 1
        elif float(data[i]) >= 40.0:
            high += 1
        elif float(data[i]) > 9:
            normal += 1
        elif float(data[i]) > 4:
            low += 1
        else: 
            very_low += 1
    return very_low, low, normal, high, very_high

