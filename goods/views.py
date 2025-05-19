from django.shortcuts import render

from goods.models import Products


# Create your views here.
def catalog(request):
    
    goods = Products.objects.all()

    context = {
        "title": "МО-ШОП — Каталог",
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "title": f"МО-ШОП — {product.name}",
        "product": product,
    }

    return render(request, "goods/product.html", context=context)
