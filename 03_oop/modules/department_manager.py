from employee import Employee


class DepartmentManager(Employee):
    def __init__(self, p_id, firstname, lastname, age, gender, salary):
        super().__init__(self, p_id, firstname, lastname, age, gender, salary)

    def __str__(self):
        super().__str__(self)
