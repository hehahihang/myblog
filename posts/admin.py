from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'created_at',
    )

    search_fields = (
        'title',
    )
# Register your models here.
