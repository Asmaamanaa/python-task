# employees = []
# while True:
#         print("Enter your choice:,1- Add new employee,2- Print all employees,3- Delete by age,4- Update Salary by name,5- End the program")
#         choice = input("Choose an option (1-5): ").strip()
    
#         if choice == '1':
#             name = input("Enter name: ")
#             age = int(input("Enter age: "))
#             salary = float(input("Enter salary: "))
#             new_employee = employees()
#             new_employee.name = name
#             new_employee.age = age
#             new_employee.salary = salary
#             employees.append(new_employee)
#         print(f"Employee {name} added successfully.")
    
#         if choice == '2':
#             if not employees:
#                 print("No employees to display.")
#         else:
#             for emp in employees:
#                 print(f"Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    
#         if choice == '3':
#             age = int(input("Enter age to delete: "))
#         original_count = len(employees)
#         employees = [emp for emp in employees if emp.age != age]
#         if len(employees) < original_count:
#             print(f"Employees aged {age} deleted successfully.")
#         else:
#             print(f"No employees aged {age} found.")
    
#         if choice == '4':
#             name = input("Enter name to update salary: ")
#         found = False
#         for emp in employees:
#             if emp.name == name:
#                 new_salary = float(input(f"Enter new salary for {name}: "))
#                 emp.salary = new_salary
#                 print(f"Salary for {name} updated to {new_salary}.")
#                 found = True
#                 break
#         if not found:
#             print(f"No employee named {name} found.")
    
#         elif choice == '5':
#             print("Ending program.")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")



choice =int()
input (" your choice ")
if choice < 1 :
    print("try again") 

choice = [1,2,3,4,5]
