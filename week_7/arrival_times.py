def arrival_times(schedule, delay):
    arrival = []
    for i in range(len(schedule)):
        split = schedule[i].split(':')
        numbers = [int(split[0]), int(split[1])]
        numbers[1] = numbers[1] + delay
        numbers[0] += (numbers[1] // 60)
        numbers[1] = numbers[1] % 60
        numbers[0] = numbers[0] % 24
        arrival.append(f'{numbers[0]:02d}:{numbers[1]:02d}')
    return arrival