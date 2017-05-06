from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.contrib import admin
from Task import models

class AttachmentInline(admin.TabularInline):
	model = models.Attachment
	fields = ('task','file','details')
	extra = 0

class CommentInline(admin.TabularInline):
	model = models.Comment
	fields = ('task','comment','created_at','updated_at')
	readonly_fields = ('created_at','updated_at')
	extra = 0

class TaskAdmin(admin.ModelAdmin):

	fieldsets = (
		(None, {
			'fields': (('app','closed'),)
		}),
		(_(''), {
			'fields': (('title',),('status','_type'),)
		}),
		(_(''), {
			'fields': (('description', 'labels'),),
		}),
	)

	list_display = ('task_code','title','app','_type','status','label','created_at','updated_at','closed')
	search_fields = ('title','app__project__name','app__name')
	list_filter = ('created_at','updated_at','closed','labels','_type','app__project__name','app')

	inlines = [AttachmentInline,CommentInline]

	def task_code(self, obj):
		return '#' + str(obj.app.project.id) + str(obj.app.id)  + '-' + str(obj.id)

	def label(self, obj):
		strg = ""
		for label in obj.labels.all():
			strg += '<b style="background:{};border-radius:15px;padding:5px;color:white;margin:5px;">{}</b>'.format(label.color, label.name)
		return strg
	label.allow_tags = True



admin.site.register(models.Task, TaskAdmin)

