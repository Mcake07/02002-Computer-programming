from wind_chill import wind_chill

output = wind_chill(-3.6, 25.6)
expected = "-4 degrees with 26 km/h wind feels like -11 degrees."
if output != expected:
    print("Failed test with wind_chill(-3.6, 25.6) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("Test passed with wind_chill(-3.6, 25.6) as it returned:")
    print(output)

output = wind_chill(-2.1, 15.0)
expected = "-2 degrees with 15 km/h wind feels like -7 degrees."
if output != expected:
    print("Failed test with wind_chill(-2.1, 15.0) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("Test passed with wind_chill(-2.1, 15.0) as it returned:")
    print(output)

expected = "-15 degrees with 58 km/h wind feels like -30 degrees."
output = wind_chill(-15.4, 58.2)
if output != expected:
    print("Failed test with wind_chill(-15.4, 58.2) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("Test passed with wind_chill(-15.4, 58.2) as it returned:")
    print(output)   

expected = "-6 degrees with 20 km/h wind feels like -13 degrees."
output = wind_chill(-5.8, 20.0)
if output != expected:
    print("Failed test with wind_chill(-5.8, 20.0) as it returned:")
    print(output)
    print("but it should have returned:")
    print(expected)
else:
    print("Test passed with wind_chill(-5.8, 20.0) as it returned:")
    print(output)