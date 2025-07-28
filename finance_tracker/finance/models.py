from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __Str__(self):
        return self.name

class Transaction(models.Model):
    TYPE_CHOICES=(('income','Income'),('expense','Expense'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()
    type=models.CharField(max_length=7,choices=TYPE_CHOICES)
    description=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.type} {self.amount}"    