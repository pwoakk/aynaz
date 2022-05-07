from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from .models import Product, Category
from django.views import generic, View


# Create your views here.


class IndexPage(generic.TemplateView):
    template_name = "index.html"


class ProductListView(View):
    category_slug = None

    def get(self, request):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(is_active=True)
        if self.category_slug:  # есть наш слаг не пустой и пользователь выбрал какую то категорию
            category = get_object_or_404(Category, slug=self.category_slug)  # берем категории по слагу
            products = products.filter(category=category)  # берем все продукты с данной категории
        context = {
            'category': category,
            'categories': categories,
            'products': products
        }

        return render(request, 'product_list.html', context)


class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'     # стандартный это object
    # slug_field = 'id'
    # slug_url_kwarg = 'pk'     # под капотом DetailView сам вытаскивает pk




