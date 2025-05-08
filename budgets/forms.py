from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Budget
from expenses.models import Category

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'period', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BudgetForm, self).__init__(*args, **kwargs)
        
        if self.user:
            self.fields['category'].queryset = Category.objects.filter(user=self.user)
        
        # Set default dates
        today = timezone.now().date()
        if not self.instance.pk:  # Only for new budgets
            # Default to current month
            self.fields['start_date'].initial = today.replace(day=1)
            next_month = today.replace(day=28) + timedelta(days=4)
            self.fields['end_date'].initial = next_month.replace(day=1) - timedelta(days=1)
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError("Start date must be before end date.")
        
        # Check for overlapping budgets for the same category
        if self.user and 'category' in cleaned_data and start_date and end_date:
            category = cleaned_data['category']
            overlapping_budgets = Budget.objects.filter(
                user=self.user,
                category=category,
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            
            # Exclude current instance if editing
            if self.instance.pk:
                overlapping_budgets = overlapping_budgets.exclude(pk=self.instance.pk)
            
            if overlapping_budgets.exists():
                raise forms.ValidationError(
                    f"There is already a budget for {category.name} during this time period."
                )
        
        return cleaned_data