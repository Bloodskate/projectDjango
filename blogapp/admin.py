from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['author','title','updated','created','publish']
	list_editable =['title']
	list_display_links=['author','updated']
	search_fields=['title','content']
	list_filter=['author','updated']
	list_per_page=4
	
admin.site.register(BlogPost,BlogPostAdmin)