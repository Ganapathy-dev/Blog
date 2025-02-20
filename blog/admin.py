from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status')
    list_filter=('status','created','publish')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=('status','publish')

admin.site.register(Post, PostAdmin) 


@admin.register(Comment) #register using decorators 
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','created','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')



