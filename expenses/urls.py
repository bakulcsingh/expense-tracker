from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='expense-list'),
    path('new/', views.ExpenseCreateView.as_view(), name='expense-create'),
    path('<int:pk>/', views.ExpenseDetailView.as_view(), name='expense-detail'),
    path('<int:pk>/update/', views.ExpenseUpdateView.as_view(), name='expense-update'),
    path('<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense-delete'),
    
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/new/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]