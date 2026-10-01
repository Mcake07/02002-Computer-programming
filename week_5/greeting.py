def greeting(hour, minute):
    if (hour < 4 or hour >= 23) or (hour == 4 and minute < 30):
        greet = 'night'
    elif (hour == 4 and minute >= 30) or (hour > 4 and hour < 12):
        greet = 'morning'
    elif (hour >= 12 and hour < 17) or (hour == 17 and minute < 30):
        greet = 'afternoon'
    elif (hour == 17 and minute >= 30) or (hour > 17 and hour < 23):
        greet = 'evening'
    else:
        print('ERROR')
    return 'good ' + greet
print(greeting(17,30))