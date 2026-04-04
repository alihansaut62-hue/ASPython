class Employee:

    def __init__(self, name, surname, salary=5000):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Salary {self.salary}"


        
emp1 = Employee("Alihan", "Saut" , 500000)
print(emp1)