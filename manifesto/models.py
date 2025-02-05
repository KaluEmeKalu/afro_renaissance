from django.db import models
from django.utils.text import slugify

class Section(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
