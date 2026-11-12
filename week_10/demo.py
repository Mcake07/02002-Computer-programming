class MyTime:
    def __init__(self, start_hour, start_minutes, start_day): #initalizing the object
        print('initalizing!')
        self.hours = start_hour
        self.minutes = start_minutes
        self.days = start_day
    def add_hours(self, hours_added):
        self.hours += hours_added
        self.days = self.hours // 24
        self.hours = self.hours % 24 #checks if hours is over 24 and fixes
    def add_minutes(self, minutes_added):
        self.minutes += minutes_added
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
start_hour = 13 #defining start time
start_minuite = 17
start_day = 2
time = MyTime(start_hour, start_minuite, start_day) #define object with hours and minuites
print(time)
print(f'Time: {time.hours:02d}:{time.minutes:02d}, days: {time.days}')
time.add_hours(500)
time.add_minutes(500)
print(f'Time: {time.hours:02d}:{time.minutes:02d}, days: {time.days}')