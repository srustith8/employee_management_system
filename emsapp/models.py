from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User

# class Employer(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     company = models.CharField(max_length=50)
#     # number of employees associated with the employer
#     number_of_employees  = models.IntegerField(default=0, blank=True, null=True)

#     def __str__(self):
#         return self.company
 


# # profile model for fields specific to Employee
# class Employee(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


# company assets, owned by the employer
class Asset(models.Model):
    asset = models.CharField(max_length=50)
    # employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __str__(self):
        return self.asset

 

# track which asset is owned by which employee
class AssignedAsset(models.Model):
    asset = models.OneToOneField(Asset,on_delete=models.CASCADE)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee

CHOICES = (('Earned Leave','Earned Leave'),('Casual Leave','Casual Leave'),('Sick Leave','Sick Leave'),('Paid Leave','Paid Leave'))
CHOICES2 = (('Approved','Approved'),('Rejected','Rejected'),('Pending','Pending'))
class Leave(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE, null =True)
    employee_ID = models.CharField(max_length = 20)
    department = models.CharField(max_length = 15)
    designation = models.CharField(max_length = 15)
    type_of_leave = models.CharField(max_length = 15, choices = CHOICES, default = None)
    from_date = models.DateField(help_text = 'mm/dd/yy')
    to_date = models.DateField(help_text = 'mm/dd/yy')
    reporting_manager = models.CharField(max_length = 50, default = None)
    reason = models.CharField(max_length=200)
    accepted = models.CharField(max_length = 50, choices = CHOICES2, default = 'Pending')        

    def __str__(self):
        return self.employee_ID