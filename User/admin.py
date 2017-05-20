from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as django_admin
from django.contrib import admin
from User.models import User


class UserAdmin(django_admin):
	fieldsets = (
					(None, {'fields': ('username', 'password')}),
					(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
					(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
												   'groups', 'user_permissions')}),
					(_('Important dates'), {'fields': ('date_joined',)}),
				)
	readonly_fields = ('last_login','date_joined')
	def get_queryset(self, request):
		qs = super(UserAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(id=request.user.id) #hide all others user if is not superuser


	def get_fieldsets(self, request, obj=None):
		if request.user.is_superuser:
			return self.fieldsets
		else:
			return (
						(None, {'fields': ('username', 'password')}),
						(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
						(_('Important dates'), {'fields': ('date_joined',)}),
					)
				

admin.site.register(User, UserAdmin)
