weight = 80
height = 1.95
age = 19
s = 1 #woman 0 men 1

bmi = weight / (height ** 2)

print(f"BMI {bmi}")


pbf = 1.2 * bmi + 0.23 * age - 10.8 * s - 5.4

print(f"Fedtprocent {pbf}")