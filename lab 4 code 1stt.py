# Define the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Define the Job class
class Job:
    def __init__(self, designation, salary):
        self.designation = designation
        self.salary = salary


# Employee class inherits from both Person and Job
class Employee(Person, Job):
    def __init__(self, name, age, designation, salary):
        # Initialize both parent classes
        Person.__init__(self, name, age)
        Job.__init__(self, designation, salary)

    # Method to display employee details
    def display_details(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary}")


# Example usage
if __name__ == "__main__":
    # Create an Employee object with your details
    emp1 = Employee("Saliha Qureshi", 19, "Cyber Security Expert", 95000)

    # Display employee details
    emp1.display_details()
