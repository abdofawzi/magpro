from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from django.contrib import admin
from Task import models, forms
from User.models import User

class AttachmentInlineValidation(BaseInlineFormSet):
	def __init__(self, *args, **kwargs):
		super(AttachmentInlineValidation, self).__init__(*args, **kwargs)

	def clean(self):
		if any(self.errors):
			return
		super(AttachmentInlineValidation, self).clean()
		manage_owned_attachments = False
		if not self.current_user.is_superuser and self.current_user.groups.filter(name="Comments - Manage Owned Comments").exists():
			manage_owned_attachments = True
		for form in self.forms:
			if not form.is_valid():
				return 
			if form.cleaned_data and form.cleaned_data.get('DELETE'):
				if manage_owned_attachments and form.cleaned_data['id'].uploaded_by != self.current_user:
					raise ValidationError(_("Can't Delete Other Users Attachments"))

class AttachmentInline(admin.TabularInline):
	model = models.Attachment
	fields = ('task','uploaded_by','file','details')
	readonly_fields = ('uploaded_by',)
	extra = 0
	form = forms.AttachmentForm
	formset = AttachmentInlineValidation

	def get_formset(self, request, obj=None, **kwargs):
		# to pass current user
		forms.AttachmentForm.current_user = request.user
		AttachmentInlineValidation.current_user = request.user
		return super(AttachmentInline, self).get_formset(request, obj, **kwargs)


class CommentInlineValidation(BaseInlineFormSet):
	def __init__(self, *args, **kwargs):
		super(CommentInlineValidation, self).__init__(*args, **kwargs)

	def clean(self):
		if any(self.errors):
			return
		super(CommentInlineValidation, self).clean()
		manage_owned_comments = False
		if not self.current_user.is_superuser and self.current_user.groups.filter(name="Comments - Manage Owned Comments").exists():
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
		# to pass current user
		forms.CommentForm.current_user = request.user
		CommentInlineValidation.current_user = request.user
		return super(CommentInline, self).get_formset(request, obj, **kwargs)

class TaskAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (('app','closed'),)
		}),
		(_(''), {
			'fields': (('title','assigned_to'),('weight','status','type'),)
		}),
		(_(''), {
			'fields': (('description', 'labels'),),
		}),
	)

	list_display = ('code','title','weight','app','type','status','label','assigned_to','created_at','updated_at','closed')
	search_fields = ('code','title','app__project__name','app__name')
	list_filter = ('closed','type','status','labels','assigned_to','app__project__name','app','weight','created_at','updated_at')

	inlines = [AttachmentInline,CommentInline]

	def render_change_form(self, request, context, *args, **kwargs):
		if not request.user.is_superuser and (request.user.groups.filter(name='Tasks - Manage Owned Tasks').exists() or request.user.groups.filter(name='Tasks - Edit Owned Tasks').exists()):
			if 'assigned_to' in context['adminform'].form.fields.keys():
				context['adminform'].form.fields['assigned_to'].queryset = User.objects.filter(id=request.user.id)
		return super(TaskAdmin, self).render_change_form(request, context, args, kwargs)             

	def get_readonly_fields(self, request, obj=None):
		if request.user.is_superuser or obj is None:
			return self.readonly_fields
		elif request.user.groups.filter(name='Tasks - Manage Owned Tasks').exists() or  request.user.groups.filter(name='Tasks - Edit Owned Tasks').exists():
			if obj.assigned_to == request.user:
				return ('assigned_to',)
			else:
				return ('app','closed','title','assigned_to','status','type','description', 'labels')

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
			elif isinstance(instance, models.Attachment) and not instance.id: #check if is Attachment instance 
				instance.uploaded_by = request.user
			instance.save()
		formset.save_m2m()

admin.site.register(models.Task, TaskAdmin)

