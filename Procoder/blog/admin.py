from blog.models import Post, BlogComment
from django.contrib import admin

# Register your models here.

admin.site.register((BlogComment))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
