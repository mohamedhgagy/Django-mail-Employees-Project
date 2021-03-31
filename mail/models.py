from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Employees(models.Model):
    created_by=models.ForeignKey(User,related_name='employee',on_delete=models.CASCADE,null=False)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    first_name=models.CharField(max_length=50,null=False,blank=True)
    last_name=models.CharField(max_length=50,null=False,blank=True)
    email=models.CharField(max_length=100,null=False,blank=True)
    phone=models.CharField(max_length=14,null=False,blank=True)
    password1=models.CharField(max_length=32,null=False,blank=True)
    password2=models.CharField(max_length=32,null=False,blank=True)
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

