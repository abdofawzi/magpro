from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.forms import BaseInlineFormSet
from django.contrib import admin
from Task import models

class AttachmentInline(admin.TabularInline):
	model = models.Attachment
	fields = ('task','uploaded_by','file','details')
	readonly_fields = ('uploaded_by',)
	extra = 0

		
class CommentInline(admin.TabularInline):
	model = models.Comment
	fields = ('task','created_by','comment','created_at','updated_at')
	readonly_fields = ('created_by','created_at','updated_at')
	extra = 0

class TaskAdmin(admin.ModelAdmin):

	fieldsets = (
		(None, {
			'fields': (('app','closed'),)
		}),
		(_(''), {
			'fields': (('title','assigned_to'),('status','type'),)
		}),
		(_(''), {
			'fields': (('description', 'labels'),),
		}),
	)

	list_display = ('code','title','app','type','status','label','assigned_to','created_at','updated_at','closed')
	search_fields = ('code','title','app__project__name','app__name')
	list_filter = ('closed','type','status','labels','assigned_to','app__project__name','app','created_at','updated_at')

	inlines = [AttachmentInline,CommentInline]

	def label(self, obj): # change label style with label color
		strg = ""
		for label in obj.labels.all():
			strg += '<b style="background:{};border-radius:15px;padding:5px;color:white;margin:5px;">{}</b>'.format(label.color, label.name)
		return strg
	label.allow_tags = True

	def save_formset(self, request, form, formset, change): # overwrite inline instances save
		instances = formset.save(commit=False)
		for obj in formset.deleted_objects:
			obj.delete()
		for instance in instances:
			if isinstance(instance, models.Comment): #check if is Comment instance 
				instance.created_by = request.user
			elif isinstance(instance, models.Attachment): #check if is Attachment instance 
				instance.uploaded_by = request.user
			instance.save()
		formset.save_m2m()


admin.site.register(models.Task, TaskAdmin)

