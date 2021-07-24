from .models import Category

def category_links(request):
    category_objects = Category.objects.all()
    return dict(category_objects=category_objects)
