class Department:
    def __int__(self, d_id, name, employees, department_manager):
        self.d_id = d_id
        self.name = name
        self.employees = employees
        self.department_manager = department_manager

    def __str__(self):
        return f'{self.d_id}: {self.name}\n  manager: {self.department_manager}'
