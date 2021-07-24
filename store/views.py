from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        product_count = products.count()

    context = {
    'products':products,
    'product_count':product_count,
    }
    print(context)
    return render(request,'store/store.html', context)
# Create your views here.

def product_detail_from_slug(request, category_slug = None, product_slug = None):
    try:
        product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    context = {
    'single_product':product,
    }
    print(context)
    return render(request, 'store/product-detail.html', context)
