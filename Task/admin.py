from __future__ import unicode_literals
from django.contrib import admin
from Task import models

class TaskAdmin(admin.ModelAdmin):
	list_display = ('fk_app','label','name','created_at','updated_at','done')
	search_fields = ('name','fk_lable__name','fk_app__fk_project__name','fk_app__name')
	list_filter = ('created_at','updated_at','done','fk_label__name','fk_app__fk_project__name','fk_app')

	def label(self, obj):
	    return '<b style="color:{};">{}</b>'.format(obj.fk_label.color, obj.fk_label.name)
	label.allow_tags = True


admin.site.register(models.Task, TaskAdmin)

