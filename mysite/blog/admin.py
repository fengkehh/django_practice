from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # Specify that it displays title, slug, author, publish and status fields
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # Specifies filter options to be displayed on the right side panel
    list_filter = ('status', 'created', 'publish', 'author')
    # Activate search bar to search title and body
    search_fields = ('title', 'body')
    # generate slug field automatically using title during add
    prepopulated_fields = {'slug': ('title',)}
    # allow author lookup then post with his author id
    raw_id_fields = ('author',)
    # display a date hierarchy bar using publish date
    date_hierarchy = 'publish'
    # Default order first by status, then publish
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)