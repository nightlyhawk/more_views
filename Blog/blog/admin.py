from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ['íd', 'title']
  search_fields = ['title', 'çontent']
 
admin.site.register(Post, PostAdmin)