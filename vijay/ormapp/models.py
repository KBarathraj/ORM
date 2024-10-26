from django.db import models
from django.contrib import admin
class Bank(models.Model):
    Name=models.CharField(max_length=15)
    AdhaarNumber=models.IntegerField(primary_key="AdhaarNumber",default=0)
    LoanAmount=models.IntegerField(default=0)
    DOB=models.DateField()
    Email=models.EmailField()
    phone=models.IntegerField()
    AccountNumber=models.IntegerField(default=0)
class BankAdmin(admin.ModelAdmin):
	list_display = ('Name','AdhaarNumber','LoanAmount','DOB','phone','Email','AccountNumber')