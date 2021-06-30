from blog.models import Post, BlogComment
from django.contrib import admin

# Register your models here.

admin.site.register((Post, BlogComment))
