def state_duration(state,timestamp):
    duration0 = 0
    duration1 = 0
    duration2 = 0
    for i in range(len(state)-1):
        if state[i] == 2:
            duration2 =+ timestamp[i+1]-timestamp[i]
        elif state[i] == 1:
            duration1 =+ timestamp[i+1]-timestamp[i]
        elif state[i] == 0:
            duration0 =+ timestamp[i+1]-timestamp[i]
        else:
            return 'ERROR'
    return 'format: 2,1,0. ', duration2, duration1, duration0

print(state_duration([1, 0, 1, 2, 1, 0],[0, 405, 515, 825, 2430, 3060]))