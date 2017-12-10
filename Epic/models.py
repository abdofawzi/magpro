# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from Project.models import Project
from Setting.models import Label
from django.db import models
from ckeditor.fields import RichTextField


class Actor(models.Model):
	project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='actor_project')
	name = models.CharField(max_length=100,verbose_name=_('Actor Name'))
	description = models.TextField(blank=True, null=True ,verbose_name=_('Description'))

	def __unicode__(self):
		return "%s-%s" % (unicode(self.project),unicode(self.name))

	class Meta:
		verbose_name = _('Actor')
		verbose_name_plural = _('Actors')


class Epic(models.Model):
	project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='epic_project')
	title = models.CharField(max_length=100,verbose_name=_('Title'))
	description = RichTextField(blank=True, null=True ,verbose_name=_('Description'))
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "%s-%s" % (unicode(self.project),unicode(self.title))

	class Meta:
		verbose_name = _('Epic')
		verbose_name_plural = _('Epics')


class UserStory(models.Model):
	epic = models.ForeignKey(Epic, verbose_name=_('Epic'), related_name='user_story_epic')
	actor = models.ForeignKey(Actor,verbose_name=_('As a'))
	want_to = models.CharField(max_length=100, verbose_name=_('Want to'))
	so_that = models.TextField(blank=True, null=True ,verbose_name=_('So that'))
	description = RichTextField(blank=True, null=True ,verbose_name=_('Description')) 
	labels = models.ManyToManyField(Label, blank=True, verbose_name=_('Label'), related_name='user_story_labels') 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return "As a (%s) want to (%s)" % (unicode(self.actor), unicode(self.want_to))

	class Meta:
		verbose_name = _('User Story')
		verbose_name_plural = _('User Stories')


