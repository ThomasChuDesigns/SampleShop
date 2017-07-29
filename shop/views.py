from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

# Get List of Products and filter if category is given
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Get products based on category slug given
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    print(request.session.keys())

    return render(request, 'shop/product/list.html', {'category':category,
                                                      'categories':categories,
                                                      'products':products})

# Get product detail page
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'shop/product/detail.html', {'product':product, 'cart_form': cart_product_form})

