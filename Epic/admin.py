from __future__ import unicode_literals
from django.utils.translation import  ugettext_lazy as _
from django.contrib import admin
from Epic import models
from Task.models import Task


class ActorAdmin(admin.ModelAdmin):
	list_display = ('project','name','description',)
	search_fields = ('project__name','name','description',)
	list_filter = ('project__name',)


class UserStoryInline(admin.TabularInline):
	model = models.UserStory
	fields = ('epic','actor','want_to','so_that','description','labels','created_at','updated_at',)
	readonly_fields = ('created_at','updated_at',)
	extra = 0


class EpicAdmin(admin.ModelAdmin):
	list_display = ('project','title','description',)
	search_fields = ('project__name','title','description',)
	list_filter = ('created_at','updated_at','project__name','user_story_epic__actor__name','user_story_epic__labels',)

	inlines = [UserStoryInline,]


class TaskInline(admin.TabularInline):
	model = Task
	fields = ('closed','code','user_story','app','title','assigned_to','weight','status','type','labels','description','created_at','updated_at',)
	readonly_fields = ('code','closed','created_at','updated_at',)
	extra = 0


class UserStoryAdmin(admin.ModelAdmin):
	list_display = ('epic','actor','want_to','so_that','label','created_at','updated_at',)
	search_fields = ('epic','actor__name','want_to','description',)
	list_filter = ('created_at','updated_at','epic__project__name','actor__name','labels',)

	def label(self, obj): # change label style with label color
		strg = ""
		for label in obj.labels.all():
			strg += '<b style="background:{};border-radius:15px;padding:5px;color:white;margin:5px;">{}</b>'.format(label.color, label.name)
		return strg
	label.allow_tags = True

	inlines = [TaskInline,]


admin.site.register(models.Actor, ActorAdmin)
admin.site.register(models.Epic, EpicAdmin)
admin.site.register(models.UserStory, UserStoryAdmin)



