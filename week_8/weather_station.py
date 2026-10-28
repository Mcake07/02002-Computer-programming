weather_station = {
    'station_name' : 'CPH Airport weather station',
    'is_operational' : True,
    'city' : 'Kastrup',
    'country' : 'Denmark',
    'construction_year' : 2016,
    'temperature_readings' : [20.1, 21.3, 19.8, 22.0, 22.0],
    'wind_speed_readings' : [5.2, 3.4, 7.1, 15.6],
}

def get_average_readings(readings):
    avg_temp = sum(weather_station['temperature_readings']) / len(weather_station['temperature_readings'])
    avg_wind_speed = sum(weather_station['wind_speed_readings']) / len(weather_station['wind_speed_readings'])
    return avg_temp, avg_wind_speed


print(f"Average temperature: {get_average_readings(weather_station['temperature_readings'])[0]:.2f}°C\nAverage wind speed: {get_average_readings(weather_station['wind_speed_readings'])[1]:.2f} m/s")