from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)
admin.site.register(models.Investor)
admin.site.register(models.Originator)
admin.site.register(models.Item)
admin.site.register(models.Business)