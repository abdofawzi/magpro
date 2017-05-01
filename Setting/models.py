from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.db import models
from colorful.fields import RGBColorField


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
