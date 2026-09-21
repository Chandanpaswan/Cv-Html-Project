from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from cv.models import TimeStampedModel


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    excerpt = models.TextField(max_length=400)
    content = models.TextField(help_text="Plain text or safe HTML content.")
    category = models.CharField(max_length=80, default="SEO")
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags.")
    featured_image = models.ImageField(upload_to="blog/", blank=True)
    author = models.CharField(max_length=120, default="Chandan Kumar Paswan")
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    seo_title = models.CharField(max_length=180, blank=True)
    meta_description = models.CharField(max_length=320, blank=True)
    og_image = models.ImageField(upload_to="blog/og/", blank=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.seo_title:
            self.seo_title = self.title
        if not self.meta_description:
            self.meta_description = self.excerpt
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    @property
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]
