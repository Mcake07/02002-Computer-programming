def wind_chill(T, v):
    T_chill = 13.12 + 0.6215 * T - 11.73 * v ** 0.16 + 0.3965 * T * v ** 0.16
    return str(round(T)) + ' degrees with ' + str(round(v)) + ' km/h of wind feels like ' + str(round(T_chill)) + ' degrees'

# -4 degrees with 26 km/h wind feels like -11 degrees.