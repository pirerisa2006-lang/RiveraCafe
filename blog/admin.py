from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "post_categories")
    list_filter = ("categories", "author")
    search_fields = ("title", "content")
    readonly_fields = ("published",)

    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all())
    post_categories.short_description = "Categorías"
