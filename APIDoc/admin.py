from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.contrib import admin
from APIDoc import models

class ParameterInline(admin.TabularInline):
	model = models.Parameter
	fields = ('route','name','type','description')
	extra = 0

class ResponseInline(admin.TabularInline):
	model = models.Response
	fields = ('route','http_status','description')
	extra = 0

class RouteAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (('app',),('title',),)
		}),
		(_(''), {
			'fields': (('method','url'),)
		}),
		(_(''), {
			'fields': ('description',),
		}),
	)

	list_display = ('app','method','url','parameters','description')
	search_fields = ('app__project__name','app__name','method','url','description')
	list_filter = ('method','app__project__name','app__name',)

	def parameters(self, obj): # list_display with all parameters
		strg = ""
		for parameter in obj.parameter_route.all():
			strg += '<b style="">-  {}<br></b>'.format(parameter.name)
		return strg
	parameters.allow_tags = True

	inlines = [ParameterInline,ResponseInline]


admin.site.register(models.DataType)
admin.site.register(models.HTTPStatus)
admin.site.register(models.Route,RouteAdmin)
