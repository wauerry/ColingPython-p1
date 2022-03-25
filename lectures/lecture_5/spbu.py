class UniversityMember:

    base_raise = 1_000

    def __init__(self, member_id, firstname, lastname, pay):
        self.member_id = member_id
        self.firstname = firstname
        self.lastname = lastname
        self.email = f"{self.firstname[0]}{self.lastname}@spbu.ru"
        self.pay = pay

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return self.fullname()

    def raise_pay(self, raise_amount):
        self.pay += self.base_raise + raise_amount


class Lecturer(UniversityMember):
    base_raise = 3_000

    def __init__(self, member_id, firstname, lastname, pay, subject):
        super().__init__(member_id, firstname, lastname, pay)
        self.subject = subject


class Dean(UniversityMember):

    def __init__(self, member_id, firstname, lastname, pay, employees=None):
        super().__init__(member_id, firstname, lastname, pay)
        self.employees = employees or []

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_employees(self):
        return '\n'.join([emp.fullname() for emp in self.employees])


employee_1 = Lecturer(87891273, "Harry", "Potter", 100_000, "Machine learning")

dean = Dean(18273319, "John", "Doe", 200_000)

print(isinstance(dean, UniversityMember))
