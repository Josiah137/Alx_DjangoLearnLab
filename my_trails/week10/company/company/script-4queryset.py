
from departments.models import Departments, Employees

# First, get the department instance  
try:  
    hr_department = Departments.objects.get(name='HR')  # Replace 'HR' with the actual department name  
except Departments.DoesNotExist:  
    print("....Department not found.")  

# Now, retrieve employees in that department  
employees_in_hr = Employees.objects.filter(department=hr_department)  # actual filtering  

# Print out the employees in the HR department  
for emp in employees_in_hr:  
    print(emp)