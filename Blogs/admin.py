from django.contrib import admin

# Register your models here.
from .models import Blog, Comment, Reply, Category, Tags

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Reply)
admin.site.register(Tags)