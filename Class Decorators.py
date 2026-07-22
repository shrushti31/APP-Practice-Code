# Class Decorator Example

def add_details(cls):

    # Add a new method
    def display(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Course :", self.course)
        print("College :", self.college)

    # Add another method
    def welcome(self):
        print("\nWelcome", self.name, "to", self.college)

    # Attach methods to the class
    cls.display = display
    cls.welcome = welcome

    return cls


@add_details
class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.college = "MIT ADT University"


# Creating Object
s1 = Student("Shrushti", 19, "B.Tech AI & Analytics")

# Calling Decorator Methods
s1.welcome()
s1.display()