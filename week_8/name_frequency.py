def name_frequency(names):
    names_split = []
    first_names = []
    for i in range(len(names)):
        names_split = names[i].split()
        first_names.append((names_split[0].lower()).capitalize())
    freq_dic = {}
    for name in first_names:
        freq_dic[name] = first_names.count(name)
    return freq_dic

# print(name_frequency(['Liv Ea Jensen', 'Mads Oliver', 'Anna Simon', 'mads kai jensen', 'Anna Madsen']))