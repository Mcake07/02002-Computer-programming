nr_boys = 20
nr_girls = 10

if (not isinstance(nr_boys, int)) or (not isinstance(nr_girls, int)):
    print("That aint a number pal")
    quit()
elif nr_girls + nr_boys > 30:
    allowed = False
elif (nr_girls - nr_boys >= 5) or (nr_boys - nr_girls >= 5):
    allowed = False
else:
    allowed = True

print("Class with", nr_girls, "girls and", nr_boys, "boys is valid:", allowed)