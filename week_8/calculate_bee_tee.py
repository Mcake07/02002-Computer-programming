def calculate_bee_tee(person_data, name):
    place = None
    for i in range(len(person_data['names'])):
        if person_data['names'][i] == name:
            place = i
    AF = None
    BEE = None
    TEE = None

    activity_level = person_data['activity_levels'][place]
    weight = person_data['weights'][place]
    height = person_data['heights'][place]
    age = person_data['ages'][place]
    gender = person_data['genders'][place]

    if activity_level == 'sedentary': AF = 1.3
    if activity_level == 'moderate': AF = 1.5
    if activity_level == 'strenuous': AF = 2.0

    if gender == 'Male': BEE = 66 + (13.7 * weight) + (5.0 * height) - (6.8 * age)
    if gender == 'Female': BEE = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    TEE = BEE * AF

    return BEE, TEE



person_data = {
    "names": ["Jakob", "Josefine", "Morten"],
    "genders": ["Male", "Female", "Male"], 
    "ages": [25, 30, 37], 
    "weights": [70, 60, 86], 
    "heights": [175, 165, 189],
    "activity_levels": ["moderate", "strenuous", "sedentary"]
}

print(calculate_bee_tee(person_data, 'Jakob'))
print(calculate_bee_tee(person_data, 'Josefine'))
print(calculate_bee_tee(person_data, 'Morten'))