from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.utils.functional import lazy
from django.dispatch import receiver
from django.db import models
from Project.models import App
from Setting.models import Label, Status, Type
from django.db.models import Max
from User.models import User
from Epic.models import UserStory
from ckeditor.fields import RichTextField
import os


class Task(models.Model):

	# create list of tubles with priority choices
	def priority_choices():
		priority = []
		for i in range(1,10):
			priority.append((i,i))
		return priority
	PRIORITY_CHOICES = priority_choices()

	code_number = models.IntegerField(verbose_name=_('Code Number'))
	code = models.CharField(max_length=200, verbose_name=_('Code'))
	user_story = models.ForeignKey(UserStory, blank=True, null=True, verbose_name=_('User Story'), related_name='task_user_story')
	app = models.ForeignKey(App, verbose_name=_('App'), related_name='task_app')
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=5, blank=True, null=True, verbose_name=_('Priority'))
	status = models.ForeignKey(Status, blank=True, null=True, default=3, verbose_name=_('Status'), related_name='task_status')
	labels = models.ManyToManyField(Label, blank=True, verbose_name=_('Label'), related_name='task_labels') 
	type = models.ForeignKey(Type, blank=True, null=True, verbose_name=_('Type'), related_name='task_type') 
	title = models.CharField(max_length=200, verbose_name=_('Title'))
	description = RichTextField(blank=True, null=True ,verbose_name=_('Description'))
	estimated_time = models.IntegerField(blank=True, null=True, verbose_name=_('Estimated Time'),help_text=_('in hours'))
	actual_time = models.IntegerField(blank=True, null=True, verbose_name=_('Actual Time'),help_text=_('in hours'))
	closed = models.BooleanField(default=False ,verbose_name=_('Closed'))
	assigned_to = models.ForeignKey(User, blank=True, null=True, verbose_name=_('Assigned to'), related_name='task_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.code)

	class Meta:
		verbose_name = _('Task')
		verbose_name_plural = _('Tasks')

	def save(self, *args, **kwargs):
		if self.id is None:
			code_number = Task.objects.filter(app = self.app).aggregate(Max('code_number'))['code_number__max']
			if code_number is not None:
				code_number += 1
			else:
				code_number = 0
			self.code_number = code_number
			self.code = '#%s-%s' % (self.app.id,code_number)
		super(Task, self).save(*args, **kwargs) # Call the "real" save() method.


class Attachment(models.Model):
	task = models.ForeignKey(Task, verbose_name=_('Task'), related_name='attachment_task')
	file = models.FileField(upload_to='task_attachments/', verbose_name = _('File'))
	uploaded_by = models.ForeignKey(User, blank=True, null=True, verbose_name=_('Uploaded by'), related_name='attachment_user')
	details = models.TextField(blank=True, null=True ,verbose_name=_('Details'))

	def __unicode__(self):
		return unicode(self.file)

	class Meta:
		verbose_name = _('Attachment')
		verbose_name_plural = _('Attachments')


@receiver(models.signals.post_delete, sender=Attachment)
def auto_delete_file_on_delete(sender, instance, **kwargs):
	"""
	Deletes file from filesystem
	when corresponding `Attachment` object is deleted.
	"""
	if instance.file:
		if os.path.isfile(instance.file.path):
			os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Attachment)
def auto_delete_file_on_change(sender, instance, **kwargs):
	"""
	Deletes old file from filesystem
	when corresponding `Attachment` object is updated
	with new file.
	"""
	if not instance.pk:
		return False

	try:
		old_file = Attachment.objects.get(pk=instance.pk).file
	except Attachment.DoesNotExist:
		return False

	new_file = instance.file
	if not old_file == new_file:
		if os.path.isfile(old_file.path):
			os.remove(old_file.path)


class Comment(models.Model):
	task = models.ForeignKey(Task, verbose_name=_('Task'), related_name='comment_task')
	comment = models.TextField(verbose_name=_('Comment'))
	created_by = models.ForeignKey(User, blank=True, null=True, verbose_name=_('User'), related_name='comment_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s-%s" % (str(self.task),str(self.created_by.id))

	class Meta:
		verbose_name = _('Comment')
		verbose_name_plural = _('Comments')


