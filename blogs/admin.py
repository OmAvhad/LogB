from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Blogs)
admin.site.register(models.Comments)
admin.site.register(models.Likes)
admin.site.register(models.Categories)