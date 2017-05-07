from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin as django_admin
from django.contrib import admin
from User.models import User


class UserAdmin(django_admin):
    pass

admin.site.register(User, UserAdmin)
