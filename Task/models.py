from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.dispatch import receiver
from django.db import models
from Project.models import App
from Setting.models import Label, Status, Type
from User.models import User
import os


class Task(models.Model):
	code = models.CharField(max_length=200, verbose_name=_('Code'))
	app = models.ForeignKey(App, verbose_name=_('App'), related_name='task_app')
	status = models.ForeignKey(Status, blank=True, null=True, verbose_name=_('Status'), related_name='task_status')
	labels = models.ManyToManyField(Label, blank=True, null=True, verbose_name=_('Label'), related_name='task_labels') 
	type = models.ForeignKey(Type, blank=True, null=True, verbose_name=_('Type'), related_name='task_type') 
	title = models.CharField(max_length=200, verbose_name=_('Title'))
	description = models.TextField(blank=True, null=True ,verbose_name=_('Description'))
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
			task_number = len(Task.objects.filter(app__project = self.app.project))
			self.code = '#%s%s' % (str(self.app.project.id),str(task_number))
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
		return str(self.task) + 'C' + str(self.id)

	class Meta:
		verbose_name = _('Comment')
		verbose_name_plural = _('Comments')


