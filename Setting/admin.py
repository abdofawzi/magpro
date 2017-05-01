from __future__ import unicode_literals
from django.contrib import admin
from Setting import models

admin.site.register(models.Label)
admin.site.register(models.Status)

