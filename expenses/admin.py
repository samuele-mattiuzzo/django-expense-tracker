from django.contrib import admin
from expenses.models import Category, Expense

# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)
