def input_valid_int(msg):
    inp=input(msg)
    if  not inp.isdecimal:
        print("Invaled input.Try again!")
    else:
        return int(inp)
    


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __str__(self) :
        return f'emplpyee: {self.name} has age {self.age} and salary {self.salary}'
    def __repr__(self) :
        return F'Employee(name="{self.name}",age={self.age},salary={self.salary}'
class EmployeeManager():
    def __init__(self) :
        self.employees=[]
    def add_employee(self):
        print("\nenter employee data:")
        name=input("enter the name: ")
        age=input_valid_int("enter the age: ")
        salary= input_valid_int("enter the salary: ")
        self.employees.append(Employee(name,age,salary))
        
    def list_employee(self):
        if len(self.employees)== 0:
            print("\nNo employees at the moment!")
            return
        print('\n employees list :')
        for emp in self.employees:
            print(emp)
    def delete_Employees_With_age(self,age_from,age_to):
        for idx in range(len(self.employees)-1,-1,-1):
            emp=self.employees[idx]
            if age_from <= emp.age <= age_to:
                print("\tDeleting",emp.name)
                self.employees.pop(idx)

    def find_employee_by_name(self,name):
        for emp in self.employees:
            if emp.name ==name:
                return emp
            return None
    def update_salary_by_name(self,name,salary):
        emp=self.find_employee_by_name(name)
        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary=salary

        
class FrontendManager():
    def __init__(self):
        self.employee_manager=EmployeeManager()
    def print_menue(self):
        print("Program Options :")
        print("1) Add a new employee")
        print("2) list all employee")
        print("3) delete by age range ")
        print("4) update salary given a name")
        print("5) End the program")
        msg= F'Enter Your choice (from 1 to 5) :'
        return input_valid_int(msg)

        
    def run(self):
        while True:
            x=self.print_menue()
            if x ==1:
                self.employee_manager.add_employee()
            elif x ==2:
                self.employee_manager.list_employee()
            elif x == 3:
                age_from=input_valid_int("Enter age from")
                age_to =input_valid_int("Enter age to")
                self.employee_manager.delete_Employees_With_age(age_from,age_to)
            elif x ==4:
                name=input("Enter name")
                salary= input_valid_int("enter new salary:")
                self.employee_manager.update_salary_by_name()
            else:
                break




    


if __name__ == '__main__':
    app=FrontendManager()
    app.run()