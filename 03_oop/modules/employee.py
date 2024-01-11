from person import Person


class Employee(Person):
    def __init__(self, p_id, firstname, lastname, age, gender, salary):
        super().__init__(self, p_id, firstname, lastname, age, gender)
        self.salary = salary

    def __str__(self):
        return f'{super.__str__()}\n  \n  salary: {self.salary}'