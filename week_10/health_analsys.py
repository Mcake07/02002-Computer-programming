class PersonHealth:
    def __init__(self,age,height,weight,sex):
        self.age = age
        self.height = height
        self.weight = weight
        if sex == 'm':
            self.sex = 1
        if sex == 'f':
            self.sex = 0
    def body_mass_index(self):
        self.bmi = self.weight / (self.height ** 2)
        return self.bmi
    def body_fat_percentage(self):
        self.bfp = 1.2 * self.body_mass_index() + 0.23 * self.age - 10.8 * self.sex - 5.4
        return self.bfp
    def get_health_description(self):
        self.bmi = self.body_mass_index()
        self.bfp = self.body_fat_percentage()
        print(f'Age: {self.age}, BMI: {self.bmi:.2f}, BFP: {self.bfp:.2f}')


person1 = PersonHealth(20, 1.70, 69, 'f')
person1.get_health_description()
person2 = PersonHealth(61, 1.92, 91, 'm')
person2.get_health_description()