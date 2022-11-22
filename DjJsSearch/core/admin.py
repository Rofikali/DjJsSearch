from django.contrib import admin

# Register your models here.
from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
