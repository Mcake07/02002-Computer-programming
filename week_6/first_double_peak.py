def first_double_peak(sequence): 
    for i in range(2, len(sequence)):
        if sequence[i] > sequence[i-1] and sequence[i] > sequence[i-2] and sequence[i] > sequence[i+1] and sequence[i] > sequence[i+2]:
            return i
    return -1