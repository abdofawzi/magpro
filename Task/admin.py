from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django.contrib import admin
from Task import models, forms
from User.models import User

class AttachmentInline(admin.TabularInline):
	model = models.Attachment
	fields = ('task','uploaded_by','file','details')
	readonly_fields = ('uploaded_by',)
	extra = 0


class CommentInlineValidation(BaseInlineFormSet):
	def __init__(self, *args, **kwargs):
		super(CommentInlineValidation, self).__init__(*args, **kwargs)

	def clean(self):
		if any(self.errors):
			return
		super(CommentInlineValidation, self).clean()
		manage_owned_comments = False
		if not self.current_user.is_superuser and len(self.current_user.groups.filter(name="Manage Owned Comments")):
			manage_owned_comments = True
		for form in self.forms:
			if not form.is_valid():
				return 
			if form.cleaned_data and form.cleaned_data.get('DELETE'):
				if manage_owned_comments and form.cleaned_data['id'].created_by != self.current_user:
					raise ValidationError(_("Can't Delete Other Users Comments"))

class CommentInline(admin.TabularInline):
	model = models.Comment
	fields = ('task','created_by','comment','created_at','updated_at')
	readonly_fields = ('created_by','created_at','updated_at')
	extra = 0
	form = forms.CommentForm
	formset = CommentInlineValidation

	def get_formset(self, request, obj=None, **kwargs):
		# to pass current user to inline form
		forms.CommentForm.current_user = request.user
		CommentInlineValidation.current_user = request.user
		return super(CommentInline, self).get_formset(request, obj, **kwargs)

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

