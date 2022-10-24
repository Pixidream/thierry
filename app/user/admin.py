"""user/admin.py
register User model in Admin Dashboard
"""
# third party
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# project module
from .models import UserProxy


admin.site.register(UserProxy, UserAdmin)
