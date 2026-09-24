question = "How many days old is Josefine?"
age = 8

days_age = age * 365
days_age_skudaar = age * 365 + age // 4

print(question)
print(f"Josefine is {age} years old, and it is {days_age} days, and accounting for leap years it is {days_age_skudaar} days")