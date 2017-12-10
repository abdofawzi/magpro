from __future__ import unicode_literals
from django.contrib import admin
from Setting import models


class LabelAdmin(admin.ModelAdmin):
	list_display = ('name','created_at','updated_at',)
	search_fields = ('created_at','updated_at',)
	list_filter = ('created_at','updated_at',)


class StatusAdmin(admin.ModelAdmin):
	list_display = ('name','created_at','updated_at',)
	search_fields = ('created_at','updated_at',)
	list_filter = ('created_at','updated_at',)


class TypeAdmin(admin.ModelAdmin):
	list_display = ('name','created_at','updated_at',)
	search_fields = ('created_at','updated_at',)
	list_filter = ('created_at','updated_at',)


admin.site.register(models.Label,LabelAdmin)
admin.site.register(models.Status,StatusAdmin)
admin.site.register(models.Type,TypeAdmin)

