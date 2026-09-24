adults = 0
childs = 0
babys = 2

birthing_capcaity = 3

runtime = 12


for month in range(runtime + 1):
    births = birthing_capcaity * adults

    adults = childs
    childs = babys
    babys = babys + births

    print('Month:', month,'Adults:', adults, 'Children:', childs, 'Babys:', babys)