from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from expenses.models import Expense, Category
from budgets.models import Budget
import json
from datetime import datetime, timedelta
from django.utils import timezone

@login_required
def dashboard(request):
    # Get date range - default to current month
    today = timezone.now().date()
    start_date = request.GET.get('start_date', today.replace(day=1).isoformat())
    end_date = request.GET.get('end_date', today.isoformat())
    
    # Convert string dates to date objects
    start_date = datetime.fromisoformat(start_date).date()
    end_date = datetime.fromisoformat(end_date).date()
    
    # Get expenses for the selected period
    expenses = Expense.objects.filter(
        user=request.user,
        date__gte=start_date,
        date__lte=end_date
    )
    
    # Total expenses for the period
    total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Expenses by category
    expenses_by_category = list(expenses.values('category__name')
                               .annotate(total=Sum('amount'))
                               .order_by('-total'))
    
    # Recent expenses
    recent_expenses = expenses.order_by('-date')[:5]
    
    # Get budgets for the period
    budgets = Budget.objects.filter(user=request.user)
    
    # Calculate budget usage
    budget_usage = []
    for budget in budgets:
        spent = expenses.filter(category=budget.category).aggregate(Sum('amount'))['amount__sum'] or 0
        budget_usage.append({
            'category': budget.category.name,
            'budget': float(budget.amount),
            'spent': float(spent),
            'remaining': float(budget.amount) - float(spent),
            'percentage': min(100, int((spent / budget.amount) * 100)) if budget.amount > 0 else 0
        })
    
    # Monthly spending trend (last 6 months)
    six_months_ago = today - timedelta(days=180)
    monthly_expenses = Expense.objects.filter(
        user=request.user,
        date__gte=six_months_ago
    ).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')
    
    # Prepare context data for the template
    context = {
        'total_spent': total_spent,
        'expenses_by_category': expenses_by_category,
        'recent_expenses': recent_expenses,
        'budget_usage': budget_usage,
        'monthly_expenses': monthly_expenses,
        'start_date': start_date,
        'end_date': end_date,
    }
    
    return render(request, 'dashboard/dashboard.html', context)