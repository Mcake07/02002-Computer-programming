def wind_chill(temperature, windspeed):
    chill = 13.12 + 0.6215 * temperature - 11.37 * windspeed ** 0.16 + 0.3965 * temperature * windspeed ** 0.16
    return f'{round(temperature)} degrees with {round(windspeed)} km/h wind feels like {round(chill)} degrees.'