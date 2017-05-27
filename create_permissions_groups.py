"""
	Intial script to create permissions groups 
"""

# DJango setting to import modules 
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PM.settings')
django.setup()

# Importing
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
# Permission = (name,content_type,codename) 
# Group = (name,permissions)

# group to manage Users
project_group, created  = Group.objects.get_or_create(name = 'Manage Users')
project_group.permissions.clear()
project_group.permissions.add(Permission.objects.get(codename = 'add_user'))
project_group.permissions.add(Permission.objects.get(codename = 'change_user'))
project_group.permissions.add(Permission.objects.get(codename = 'delete_user'))
# group to edit user information
project_group, created  = Group.objects.get_or_create(name = 'User Edit His Information')
project_group.permissions.clear()
project_group.permissions.add(Permission.objects.get(codename = 'change_user'))

# group to manage Projects 
project_group, created  = Group.objects.get_or_create(name = 'Manage Projects')
project_group.permissions.clear()
project_group.permissions.add(Permission.objects.get(codename = 'add_project'))
project_group.permissions.add(Permission.objects.get(codename = 'change_project'))
project_group.permissions.add(Permission.objects.get(codename = 'delete_project'))

# group to manage Apps
app_group, created  = Group.objects.get_or_create(name = 'Manage Apps')
app_group.permissions.clear()
app_group.permissions.add(Permission.objects.get(codename = 'add_app'))
app_group.permissions.add(Permission.objects.get(codename = 'change_app'))
app_group.permissions.add(Permission.objects.get(codename = 'delete_app'))

# group to manage Labels
labels_group, created  = Group.objects.get_or_create(name = 'Manage Labels')
labels_group.permissions.clear()
labels_group.permissions.add(Permission.objects.get(codename = 'add_label', content_type__app_label = 'Setting'))
labels_group.permissions.add(Permission.objects.get(codename = 'change_label', content_type__app_label = 'Setting'))
labels_group.permissions.add(Permission.objects.get(codename = 'delete_label', content_type__app_label = 'Setting'))
# group user can add Labels
add_labels_group, created  = Group.objects.get_or_create(name = 'Add Labels')
add_labels_group.permissions.clear()
add_labels_group.permissions.add(Permission.objects.get(codename = 'add_label', content_type__app_label = 'Setting'))

# group to manage Statuses
statuses_group, created  = Group.objects.get_or_create(name = 'Manage Statuses')
statuses_group.permissions.clear()
statuses_group.permissions.add(Permission.objects.get(codename = 'add_status'))
statuses_group.permissions.add(Permission.objects.get(codename = 'change_status'))
statuses_group.permissions.add(Permission.objects.get(codename = 'delete_status'))
# group user can add Statuses
add_statuses_group, created  = Group.objects.get_or_create(name = 'Add Statuses')
add_statuses_group.permissions.clear()
add_statuses_group.permissions.add(Permission.objects.get(codename = 'add_status'))

# group to manage Types
types_group, created  = Group.objects.get_or_create(name = 'Manage Tasks Types')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_type'))
types_group.permissions.add(Permission.objects.get(codename = 'change_type'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_type'))
# group user can add Types
add_types_group, created  = Group.objects.get_or_create(name = 'Add Tasks Types')
add_types_group.permissions.clear()
add_types_group.permissions.add(Permission.objects.get(codename = 'add_type'))

# group to manage Comments
types_group, created  = Group.objects.get_or_create(name = 'Manage Comments')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_comment', content_type__app_label = 'Task'))
types_group.permissions.add(Permission.objects.get(codename = 'change_comment', content_type__app_label = 'Task'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_comment', content_type__app_label = 'Task'))
# group user can manage owned Comments
types_group, created  = Group.objects.get_or_create(name = 'Manage Owned Comments')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_comment', content_type__app_label = 'Task'))
types_group.permissions.add(Permission.objects.get(codename = 'change_comment', content_type__app_label = 'Task'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_comment', content_type__app_label = 'Task'))

# group to manage all Attachments
types_group, created  = Group.objects.get_or_create(name = 'Manage Attachments')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_attachment'))
types_group.permissions.add(Permission.objects.get(codename = 'change_attachment'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_attachment'))
# group user can manage owned Attachments
types_group, created  = Group.objects.get_or_create(name = 'Manage Owned Attachments')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_attachment'))
types_group.permissions.add(Permission.objects.get(codename = 'change_attachment'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_attachment'))

# group to manage Tasks
types_group, created  = Group.objects.get_or_create(name = 'Manage Tasks')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_task'))
types_group.permissions.add(Permission.objects.get(codename = 'change_task'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_task'))
# group user can manage owned Tasks
types_group, created  = Group.objects.get_or_create(name = 'Manage Owned Tasks')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_task'))
types_group.permissions.add(Permission.objects.get(codename = 'change_task'))
# group user can edit owned Tasks
types_group, created  = Group.objects.get_or_create(name = 'Edit Owned Tasks')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'change_task'))

# group to manage Wiki
types_group, created  = Group.objects.get_or_create(name = 'Manage Wiki')
types_group.permissions.clear()
types_group.permissions.add(Permission.objects.get(codename = 'add_comment', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'change_comment', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_comment', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'add_label', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'change_label', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_label', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'add_wiki', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'change_wiki', content_type__app_label = 'Wiki'))
types_group.permissions.add(Permission.objects.get(codename = 'delete_wiki', content_type__app_label = 'Wiki'))


print 'Done Creating all Permissions Groups'










