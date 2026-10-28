def data_statistics(data, name):
    experiment = {}
    experiment['name'] = name
    experiment['values'] = data
    experiment['mean'] = sum(data) / len(data)
    
    x = 0
    for i in range(len(data)): x += (data[i] - experiment['mean']) ** 2
    experiment['standard_deriviation'] = (x / len(data)) ** 0.5
    experiment['max_val'] = max(data)
    experiment['min_val'] = min(data)
    return experiment

experiment_name = "standard_values"
experiment_values = [1.30, -0.01,  1.35,  0.31,  0.35, -1.61,  1.39,  1.19, -1.07,  0.34]

print(data_statistics(experiment_values, experiment_name))