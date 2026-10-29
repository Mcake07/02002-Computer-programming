def merger(phonebook, second_phonebook):
    for person in second_phonebook: #goes through second phonebook keys
        if person in phonebook:
            number_list2 = second_phonebook[person] # second phonenumber list of a person
            number_list1 = phonebook[person] # first phonenumber list of a person
            for number in number_list2: 
                if number not in number_list1:
                    number_list1.append(number)
        else:
            phonebook[person] = second_phonebook[person]
    return phonebook

phonebook = {'Liv': ['55511112', '18777890'],
             'Mads': ['27274445', '48533336'],
             'Steve': ['45455555', '25455525']}

second_phonebook = {'Anna': ['89577772'],
                    'Steve': ['25257755', '25455525'],
                    'Mads': ['48533336', '27274445']}



print(merger(phonebook, second_phonebook))