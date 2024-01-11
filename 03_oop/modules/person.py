class Person:
    possible_genders = {'m', 'f', 'd'}

    def __init__(self, p_id, firstname, lastname, age, gender):
        self.p_id = p_id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __str__(self):
        return f' {self.p_id}: {self.firstname} {self.lastname}({self.gender}) - {self.age}'
