months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_longer_than(days):
    longer_months = []
    for i in range(len(months_list)):
        if days_list[i] > days:
            longer_months.append(months_list[i])

    return longer_months

print(days_longer_than(30))
print(days_longer_than(31))
print(days_longer_than(10))