from django.contrib import admin
from django.utils.html import format_html

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "is_featured", "is_published", "action_links")
    list_filter = ("category", "is_featured", "is_published")
    list_editable = ("is_featured", "is_published")
    search_fields = ("title", "excerpt", "content", "tags")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    fieldsets = (("Article", {"fields": ("title", "slug", "excerpt", "content", "category", "tags", "featured_image", "author")}), ("Publishing", {"fields": ("published_at", "is_featured", "is_published")}), ("SEO", {"fields": ("seo_title", "meta_description", "og_image")}))

    @admin.display(description="Actions")
    def action_links(self, obj):
        change_url = f"/admin/blog/blogpost/{obj.pk}/change/"
        delete_url = f"/admin/blog/blogpost/{obj.pk}/delete/"
        return format_html(
            '<div class="action-links"><a href="{}">Edit</a><a href="{}" class="delete-link">Delete</a></div>',
            change_url,
            delete_url,
        )
