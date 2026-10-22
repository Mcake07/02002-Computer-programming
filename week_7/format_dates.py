def format_date(date):
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
    date_splitted = date.split('/')
    if len(date_splitted[0]) == 4:
        date_adjusted = date_splitted[2] + '-' + month[int(date_splitted[1])-1] + '-' + date_splitted[0][2:4]
    else:
        date_adjusted = date_splitted[0] + '-' + month[int(date_splitted[1])-1] + '-' + date_splitted[2][2:4]
    return date_adjusted

print(format_date('11/12/1999'))
print(format_date('2007/04/04'))