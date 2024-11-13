from django.db import models

# Create your models here.
class Departments(models.Model):
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.department_name}")
    
class Employees(models.Model):
    employee_name = models.CharField(max_length=100)
    # employee_id = models.IntegerField()
    employee_position = models.CharField(max_length=70)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name = "worker")

    def __str__(self):
       return (f"{self.employee_name}, {self.employee_position}")
    


