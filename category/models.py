from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    slug = models.SlugField(blank=False, null=False, unique=True)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank=True)

    class Meta:
     verbose_name = 'category'
     verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
