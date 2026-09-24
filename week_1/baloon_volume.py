#input
n = float(input("How many moles of gas?: ")) #rigtige er  0.692
T = float(input("What is the temperature of the gas (kelvin): ")) #rigtige er 280
P = float(input("What is the temperature of the gas (bar): ")) # rigtige er 0.81

#konstanter
R = 0.0831

#Beregning
V = (n * R * T) / P

print("Volumen er: " + str(V) + "l")