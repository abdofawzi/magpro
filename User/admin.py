from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin as django_admin
from django.contrib import admin
from User.models import User


class UserAdmin(django_admin):

	def get_queryset(self, request):
		qs = super(UserAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(id=request.user.id) #hide all others user if is not superuser


admin.site.register(User, UserAdmin)
