#Input
T = float(input("What should the time period be (years)?: "))
n = float(input("What should the amount of times that the event happens in a period of " + str(T) + " years?: "))

#Beregning
P = 1 - ((1 - (1 / T)) ** n)




print("The propability of the event happens " + str(n) + " time(s) every " + str(T) + " year(s), is: " + str(P * 100) + "%")