debt = 1000
debt_initial = debt
monthly_payment = 100
interest = 0.05
months = 0

if (monthly_payment - (interest * debt)) <= 0:
    print('Too little of a monthly payment')
    quit()
else:
    while debt > 0:
        debt = debt * (1 + interest)
        debt = debt - monthly_payment
        months += 1

print(f'Debt is paid of in {months} months with an monthly payment of {monthly_payment} a month, interest at {interest} and an initial debt of {debt_initial}')