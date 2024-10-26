from django.db import models
from django.contrib import admin
class Bank(models.Model):
    Name=models.CharField(max_length=15)
    AdhaarNo=models.IntegerField(primary_key="AdhaarNo")
    LoanAmt=models.IntegerField()
    DOB=models.DateField()
    Email=models.IntegerField()
    phone=models.IntegerField()
class BankAdmin(admin.ModelAdmin):
	list_display = ('Name','AdhaarNo','LoanAmt','DOB','Email','phone')


