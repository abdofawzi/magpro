"""
	Intial script to create permissions groups 
"""

# DJango setting to import modules 
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PM.settings")
django.setup()

# Importing
from django.contrib.auth.models import Permission, Group
# Permission = (name,content_type,codename) 
# Group = (name,permissions)

ps = Permission.objects.all()
for p in ps:
	print "(%s), name= %s, condename= %s" % (p ,p.name, p.codename)

# group to manage Projects 
project_group, created  = Group.objects.get_or_create(name = 'Manage Projects')
project_group.permissions.clear()
project_group.permissions.add(Permission.objects.get(codename = "add_project"))
project_group.permissions.add(Permission.objects.get(codename = "change_project"))
project_group.permissions.add(Permission.objects.get(codename = "delete_project"))

# group to manage Apps
app_group, created  = Group.objects.get_or_create(name = 'Manage Apps')
app_group.permissions.clear()
app_group.permissions.add(Permission.objects.get(codename = "add_app"))
app_group.permissions.add(Permission.objects.get(codename = "change_app"))
app_group.permissions.add(Permission.objects.get(codename = "delete_app"))

# group to manage Labels
labels_group, created  = Group.objects.get_or_create(name = 'Manage Labels')
labels_group.permissions.clear()
labels_group.permissions.add(Permission.objects.get(codename = "add_app"))
labels_group.permissions.add(Permission.objects.get(codename = "change_app"))
labels_group.permissions.add(Permission.objects.get(codename = "delete_app"))
# group to add Labels
add_labels_group, created  = Group.objects.get_or_create(name = 'Add Labels')
add_labels_group.permissions.clear()
add_labels_group.permissions.add(Permission.objects.get(codename = "add_app"))

# group to manage Statuses
statuses_group, created  = Group.objects.get_or_create(name = 'Manage Statuses')
statuses_group.permissions.clear()
statuses_group.permissions.add(Permission.objects.get(codename = "add_status"))
statuses_group.permissions.add(Permission.objects.get(codename = "change_status"))
statuses_group.permissions.add(Permission.objects.get(codename = "delete_status"))
# group to add Statuses
add_statuses_group, created  = Group.objects.get_or_create(name = 'Add Statuses')
add_statuses_group.permissions.clear()
add_statuses_group.permissions.add(Permission.objects.get(codename = "add_status"))

# group to manage Types
types_group, created  = Group.objects.get_or_create(name = 'Manage Tasks Types')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = "add_type"))
types_group.permissions.add(Permission.objects.get(codename = "change_type"))
types_group.permissions.add(Permission.objects.get(codename = "delete_type"))
# group to add Types
add_types_group, created  = Group.objects.get_or_create(name = 'Add Tasks Types')
add_types_group.permissions.clear()
add_types_group.permissions.add(Permission.objects.get(codename = "add_type"))










