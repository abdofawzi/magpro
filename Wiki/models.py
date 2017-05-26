from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.db import models
from colorful.fields import RGBColorField
from User.models import User

class Label(models.Model):
	name = models.CharField(max_length=100, verbose_name=_('Label Name'))
	color = RGBColorField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name = _('Label')
		verbose_name_plural = _('Labels')

class Wiki(models.Model):
	title = models.CharField(max_length=200, verbose_name=_('Title'))
	content = models.TextField(verbose_name=_('Content'))
	labels = models.ManyToManyField(Label, blank=True, verbose_name=_('Label'), related_name='wiki_labels') 
	created_by = models.ForeignKey(User, blank=True, null=True, verbose_name=_('Created by'), related_name='wiki_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.id) + '-' + str(self.title)

	class Meta:
		verbose_name = _('Wiki')
		verbose_name_plural = _('Wikis')

class Comment(models.Model):
	wiki = models.ForeignKey(Wiki, verbose_name=_('Wiki'), related_name='comment_wiki')
	comment = models.TextField(verbose_name=_('Comment'))
	created_by = models.ForeignKey(User, blank=True, null=True, verbose_name=_('User'), related_name='wiki_comment_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.wiki) + 'C' + str(self.id)

	class Meta:
		verbose_name = _('Comment')
		verbose_name_plural = _('Comments')


