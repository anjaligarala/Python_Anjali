class Employee:
    'Common base class of all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, "Salary :", self.salary)


print("Employee.__doc__ : ", Employee.__doc__)  # Class documentation string or none, if undefined.
print("Employee.__name__ : ", Employee.__name__)  # Class name
print("Employee.__module__ : ",
      Employee.__module__)  # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print("Employee.__bases__ : ",
      Employee.__bases__)  # A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list
print("Employee.__dict__ : ", Employee.__dict__)  # Dictionary containing the class's namespace.
