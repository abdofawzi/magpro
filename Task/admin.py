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
			'fields': (('app',),)
		}),
		(_(''), {
			'fields': (('title','closed'),('status',),)
		}),
		(_(''), {
			'fields': (('description', 'labels'),),
		}),
	)

	list_display = ('task_code','app','label','title','created_at','updated_at','closed')
	search_fields = ('title','app__project__name','app__name')
	list_filter = ('created_at','updated_at','closed','labels','app__project__name','app')

	inlines = [AttachmentInline,CommentInline]

	def task_code(self, obj):
		return '#' + str(obj.id)

	def label(self, obj):
		strg = ""
		for label in obj.labels.all():
			strg += '<b style="background:{};border-radius:15px;padding:5px;color:white;margin:5px;">{}</b>'.format(label.color, label.name)
			# strg += '<b style="color:{};">{}&nbsp;</b>'.format(label.color, label.name)
		return strg
	label.allow_tags = True



admin.site.register(models.Task, TaskAdmin)

