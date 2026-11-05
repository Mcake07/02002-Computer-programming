def count_differences(filename1, filename2):
    with open(filename1) as f:
        contents1 = f.read()
    with open(filename2) as f:
        contents2 = f.read()
    list1 = contents1.split(', ')
    list2 = contents2.split(', ')
    if len(list1) != len(list2): 
        return -1
    different_amount = 0
    for i in range(len(list1)):
        list1[i] = float(list1[i])
        list2[i] = float(list2[i])
        if list1[i] != list2[i]:
            different_amount += 1
    return different_amount