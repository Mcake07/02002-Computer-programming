#Consider a train that is scheduled to arrive at 21:30. That is, hours is 21 and minutes is 30.
#What is the expected arrival time if the train is delayed by 17 minutes?
#What is the expected arrival time if the train is delayed by 35 minutes?
#Identify other special cases that the code needs to be able to handle?
#Write down your results. Also write down all intermediate calculations. Can you identify a general approach that will work for all cases?

hour = 21
minute = 30

delay17_minute = (minute + 17) % 60
delay17_hour = (minute + 17) // 60

delay35_minute = (minute + 35) % 60
delay35_hour = (minute + 35) // 60

print(str(hour) + ":" + str(minute))
print(str(delay17_hour) + ":" + str(delay17_minute))
print(str(delay35_hour) + ":" + str(delay35_minute))

print(f"test {hour ** 2}")