temperature = 37
state = "Normal"

if (not isinstance(temperature, float)) and (not isinstance(temperature, int)):
    print("That aint a number pal")
    quit()
elif temperature <= 35:
    state = "Hypothermia"
elif temperature >= 37.5 and temperature < 40:
    state = "Hyperthermia"
elif temperature >= 40:
    state = "Hyperpyrexia"
else:
    state = "Normal"

print("The temperature", temperature, "is", state)