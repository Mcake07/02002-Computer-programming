class MyTime:
    def __init__(self, start_hour, start_minute):
        self.hours = start_hour
        self.minutes = start_minute
        self.days = 0
    def get_time(self): return (self.hours, self.minutes)
    def increment_hours(self, hours_added):
        self.hours += hours_added
        self.days += self.hours // 24
        self.hours = self.hours % 24
    def increment_minutes(self, minutes_added):
        self.minutes += minutes_added
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.days += self.hours // 24
        self.hours = self.hours % 24
class WorldTime(MyTime):
    def __init__(self, start_hour, start_minute, clock_type):
        super().__init__(start_hour,start_minute)
        self.clock_type = clock_type
    def __str__(self):
        if self.clock_type == '24':
            return f'{self.hours:02d}:{self.minutes:02d}'
        else:
            am_pm = ''
            h = self.hours
            if self.hours > 12:
                h -= 12
                am_pm = 'PM'
            else:
                am_pm = 'AM'
            if h == 0:
                h = 12
            return f'{h:02d}:{self.minutes} {am_pm}'

start_hour = 13
start_minute = 15
clock_type = '12'
world_time = WorldTime(start_hour, start_minute, clock_type)
print(str(world_time))