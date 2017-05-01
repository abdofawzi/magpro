from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.db import models
from Project.models import App
from Setting.models import Label


class Task(models.Model):
	fk_app = models.ForeignKey(App, verbose_name=_('App'), related_name='app_task')
	fk_label = models.ForeignKey(Label, blank=True, null=True, verbose_name=_('Label'), related_name='app_label') 
	name = models.CharField(max_length=100, verbose_name=_('Task Name'))
	description = models.TextField(blank=True, null=True ,verbose_name=_('Description'))
	done = models.BooleanField(default=False ,verbose_name=_('Done'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name = _('Task')
		verbose_name_plural = _('Tasks')
