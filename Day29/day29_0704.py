class Employee:
    empCount = 0

    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    # def displayCount(self):
    # print("Total Employee % d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, "Salary: ", self.salary, "Age: ", self.age)


emp1 = Employee("Anjali", 2000, 27)
emp2 = Employee("Sohil", 1000, 30)
emp1.displayEmployee()
# emp2.displayEmployee()
x = getattr(emp2, 'age')
print(x)
hasattr(emp2, 'name')
print("Total Employee % d" % Employee.empCount)
