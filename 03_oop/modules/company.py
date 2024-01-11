from person import Person
from department_manager import DepartmentManager


class Company:
    def __init__(self, c_id, c_name, employees, departments):
        self.c_id = c_id
        self.c_name = c_name
        self.employees = employees
        self.departments = departments

    def count_staff(self, department_managers=True, employees=True):
        if department_managers:
            cnt_department_managers = 0
            for employee in self.employees:
                if isinstance(employee, DepartmentManager):
                    cnt_department_managers += 1

            if employees:
                # return department_managers and employees
                return cnt_department_managers, len(self.employees)

            else:
                # department_managers only
                return cnt_department_managers

        if employees:
            # employees only
            return len(self.employees)

    def count_departments(self):
        return len(self.departments)

    def biggest_department(self):
        # can return either a single department or a list of them
        # maybe return always a list
        # TODO: is there a cleaner way to do (see context above)?

        biggest_dep = None
        biggest_dep_size = 0
        for dep in self.departments:
            size = len(dep.employees)
            if size > biggest_dep_size:
                biggest_dep = dep
                biggest_dep_size = size

            elif size == biggest_dep_size:
                biggest_dep.append(dep)

        return biggest_dep

    def gender_distribution(self):
        distributions = {}
        for gender in Person.possible_genders:
            cnt_employees = None
            for employee in self.employees:
                if employee.gender == gender:
                    cnt_employees += 1

            distributions[gender] = cnt_employees / len(self.employees)
        
        return distributions
