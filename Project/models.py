from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=100, verbose_name=_('Project Name'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name = _('Project')
		verbose_name_plural = _('Projects')

class App(models.Model):
	project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_app')
	name = models.CharField(max_length=100, verbose_name=_('App Name'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return unicode(self.project.name) + '-' + unicode(self.name)

	class Meta:
		verbose_name = _('App')
		verbose_name_plural = _('Apps')







