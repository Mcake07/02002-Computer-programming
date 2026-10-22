examples = ['Holte_2840', 'Kongens Lyngby 2800', 'Torshavn 100', '2400_Kobenhavn_Nordvest']

def standardize_address(address):
    address = address.replace('_', ' ')
    address_split = address.split()
    numbers = '1234567890'
    if address_split[0][0] in numbers: # [0][0] er fordi at man tager det første tegn i den første entry
        return address
    else:
        postal_code = address_split[-1]
        city_parts = address_split[:-1]
        city = ' '.join(city_parts)
        return postal_code + ' ' + city


for i in examples:
    print(f' Example: {i}, Answer: {standardize_address(i)}')