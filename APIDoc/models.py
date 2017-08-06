from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.db import models
from Project.models import *

class HTTPStatus(models.Model):
	code = models.IntegerField(verbose_name=_('Code'))
	status = models.CharField(max_length=100, verbose_name=_('Status'))

	def __unicode__(self):
		return "%s %s" % (str(self.code),str(self.status))

	class Meta:
		verbose_name = _('HTTP Status')
		verbose_name_plural = _('HTTP Statuses')

class Route(models.Model):
	method_choices = (
		('GET','GET'),
		('POST','POST'),
		('PATCH','PATCH'),
		('PUT','PUT'),
		('DELETE','DELETE'),
		)

	app = models.ForeignKey(App, verbose_name=_('App'), related_name='route_app')
	method = models.CharField(max_length=20,choices=method_choices, verbose_name=_('Method'))
	url = models.CharField(max_length=100, verbose_name=_('Base URL'))
	description = models.TextField(blank=True, null=True ,verbose_name=_('Description'))

	def __unicode__(self):
		return "%s [%s] %s" % (str(self.description),str(self.method), str(self.url))

	class Meta:
		verbose_name = _('Route')
		verbose_name_plural = _('Routes')

class Parameter(models.Model):
	route = models.ForeignKey(Route, verbose_name=_('Route'), related_name='parameter_route')
	name = models.CharField(max_length=20, verbose_name=_('Description'))
	description = models.TextField(blank=True, null=True ,verbose_name=_('Description'))

	def __unicode__(self):
		return str(self.name)

	class Meta:
		verbose_name = _('Parameter')
		verbose_name_plural = _('Parameters')

class Response(models.Model):
	route = models.ForeignKey(Route, verbose_name=_('Route'), related_name='response_route')
	http_status = models.ForeignKey(HTTPStatus, verbose_name=_('HTTP Status'), related_name='base_url_default_response')
	description = models.TextField(blank=True, null=True ,verbose_name=_('Description'))

	def __unicode__(self):
		return str(self.http_status)

	class Meta:
		verbose_name = _('Response')
		verbose_name_plural = _('Responses')



