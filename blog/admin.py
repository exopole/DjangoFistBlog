from django.contrib import admin
from .models import Post


def apply_publish(modeladmin, request, queryset):
    for post in queryset:
        post.publish()

apply_publish.short_description = 'Publish'

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'author']
    actions = [apply_publish, ]  # <-- Add the list action function here
    #fields = ['author', 'title', 'created_date', 'published_date']


admin.site.register(Post, PostAdmin)
#admin.site.register(Post)
