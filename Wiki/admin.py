from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from pagedown.widgets import AdminPagedownWidget
from django.contrib import admin
from django.db import models as django_models
from Wiki import models

class CommentInline(admin.TabularInline):
	model = models.Comment
	fields = ('wiki','created_by','comment','created_at','updated_at')
	readonly_fields = ('created_by','created_at','updated_at')
	extra = 0

class WikiAdmin(admin.ModelAdmin):
	formfield_overrides = {
		django_models.TextField: {'widget': AdminPagedownWidget },
	}
	fieldsets = (
		(None, {
			'fields': (('title','labels'),)
		}),
		(_(''), {
			'fields': ('content',)
		}),
	)

	list_display = ('title','label','created_by','created_at','updated_at')
	search_fields = ('title','created_by')
	list_filter = ('labels','created_by','created_at','updated_at')

	inlines = [CommentInline]

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
			if isinstance(instance, models.Comment) and not instance.id: #check if is Comment instance 
				instance.created_by = request.user
			instance.save()
		formset.save_m2m()

admin.site.register(models.Wiki, WikiAdmin)
admin.site.register(models.Label)
