class EmployeeSalary:
    hourly_payment = 400  

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=None, email=None):
        if hours is None and rest_days is not None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours=None, rest_days=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment
    
    # Пример использования

# Сотрудник без часов, но с выходными
emp1 = EmployeeSalary.get_hours("Анна", rest_days=2)
print(emp1.hours)  # 40 (5 дней * 8 часов)
print(emp1.salary())  # 40 * 400 = 16000

# Сотрудник без email
emp2 = EmployeeSalary.get_email("Иван", hours=32)
print(emp2.email)  # Иван@email.com

# Изменение ставки
EmployeeSalary.set_hourly_payment(500)
print(emp2.salary())  # 32 * 500 = 16000

# Проверка, что ставка изменилась для всех
emp3 = EmployeeSalary("Мария", 10)
print(emp3.salary())  # 10 * 500 = 5000