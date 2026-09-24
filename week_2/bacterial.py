bac_start = 500000000
bac_growth_minmax = [600000000, 800000000]

bac_time = 2

bac_min_now = bac_start + min(bac_growth_minmax) * bac_time
bac_max_now = bac_start + max(bac_growth_minmax) * bac_time


bac_current = 1500000000


contaminated = bac_current < bac_min_now or bac_current > bac_max_now


if contaminated == True :
    print("Contaminated!")

elif contaminated != True :
    print("Its fine")

else:
    print("ERROR")