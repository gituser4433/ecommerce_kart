from django.db import models
from category.models import Category
from django.utils import timezone
from django.urls import reverse
# Create your models here.
UNIT_CHOICES = (('PCS', 'PCS'), ('EACH', 'EACH'),('KG','KG'),('BOX','BOX'))
class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True, blank=False, null = False)
    slug = models.SlugField(max_length=100)
    sku = models.CharField(max_length=100, unique=True, blank = False, null = False)
    unit = models.CharField(choices=UNIT_CHOICES, null=False, blank=False, max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(blank=True, max_length=200)
    stock = models.IntegerField(null=False, blank = False)
    images = models.ImageField(upload_to='photos/products', default='DEFAULT VALUE')
    is_available = models.BooleanField(default=True)
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_by_category_and_product', args=(self.category.slug,self.slug))

    def __str__(self):
        return self.product_name
