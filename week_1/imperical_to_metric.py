print("First input feet, then inches. So if you are 5ft and 4 inches then first input 5 and then in the next input 4. ") #Hun er 5 fod 1 inch

#input
height_feet = float(input("How many feet (ignore the inches for now, DO NOT ROUND) to convert?: "))
height_inches = float(input("How many inches in excess of those feet to convert?: "))

#conversion
inch_per_foot = 12
cm_per_inch = 2.54

converted_cm = (inch_per_foot * height_feet * cm_per_inch) + (height_inches * cm_per_inch)

m = converted_cm // 100
rest_cm = converted_cm % 100

m_str = str(m)
rest_cm_str = str(rest_cm)

print("Konverteret til " + m_str + "m " + "og " + rest_cm_str + "cm")