from __future__ import unicode_literals
from django.contrib import admin
from Project import models

class AppInline(admin.TabularInline):
	model = models.App
	fields = ('project','name')
	extra = 0


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name','created_at','updated_at')
	search_fields = ('name','project_app__name')
	list_filter = ('created_at','updated_at')

	inlines = [AppInline,]



admin.site.register(models.Project, ProjectAdmin)
