from django.db import models
from django.contrib.auth.models import User
from expenses.models import Category
from django.utils import timezone
import datetime

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    
    PERIOD_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('custom', 'Custom'),
    ]
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='monthly')
    
    class Meta:
        unique_together = ('user', 'category', 'start_date', 'end_date')
    
    def __str__(self):
        return f"{self.category} - {self.amount} - {self.period}"
    
    def get_spent_amount(self):
        """Calculate how much has been spent in this budget's category during the budget period"""
        from expenses.models import Expense
        expenses = Expense.objects.filter(
            user=self.user,
            category=self.category,
            date__gte=self.start_date,
            date__lte=self.end_date
        )
        return sum(expense.amount for expense in expenses)
    
    def get_remaining_amount(self):
        """Calculate remaining budget"""
        return self.amount - self.get_spent_amount()
    
    def get_percentage_used(self):
        """Calculate percentage of budget used"""
        spent = self.get_spent_amount()
        if self.amount > 0:
            return (spent / self.amount) * 100
        return 0