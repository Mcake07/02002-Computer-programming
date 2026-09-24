age = 45
weight = 80
is_smoker = True
high_risk = True

if ((not isinstance(age, int)) and (not isinstance(age, float))) or ((not isinstance(weight, int)) and (not isinstance(weight, int))) or (not isinstance(is_smoker, bool)):
    print("That aint a number pal (or bool)")
    quit()
elif (age >= 18) and (age <= 30):
    high_risk = False
elif age < 18:
    if weight <= 60:
        high_risk = True
    else:
        high_risk = True
elif age > 30:
    if is_smoker:
        high_risk = True
    else:
        high_risk = False



print("Age", age, "weight", weight, "smoker", is_smoker, "high risk", high_risk)