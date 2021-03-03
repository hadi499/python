
class Employee:
    raise_amt = 1.4

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


dev1 = Developer('hadi', 'purnomo', 50000, 'python')
dev2 = Developer('eko', 'pradana', 43000, 'java')

mgr1 = Manager('john', 'doe', 79000, [dev1])
print(mgr1.email)
mgr1.print_emps()

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# print(dev1.prog_lang)
