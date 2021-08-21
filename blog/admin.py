from django.contrib import admin
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title', )}
    filter_horizontal = ('tags', )

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
