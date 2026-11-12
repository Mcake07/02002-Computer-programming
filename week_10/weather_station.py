class WeatherStation:
    def __init__(self, station_name, is_operational):
        self.station_name = station_name
        self.is_operational = is_operational
        self.wind_readings =[]
        self.temperature_readings = []
    def take_daily_wind_readings(self,wind_readings):
        if self.is_operational:
            self.wind_readings = wind_readings
        else:
            print('Station not operational')
    def take_daily_temperature_readings(self,temperature_readings):
        if self.is_operational:
            self.temperature_readings = temperature_readings
        else:
            print('Station not operational')
    def get_highest_reading(self):
        if len(self.wind_readings) > 0 and len(self.temperature_readings) > 0:
            return max(self.wind_readings), max(self.temperature_readings)
        else:
            print('One or more list-input is empty')

cph = WeatherStation('cph',True)
cph.take_daily_wind_readings([3.5, 6.2, 7.1, 12.1])
cph.take_daily_temperature_readings([18.1, 18.3, 19.0, 18.5])
print(cph.wind_readings, cph.temperature_readings)
max_wind, max_temp = cph.get_highest_reading()
print(max_wind,max_temp)