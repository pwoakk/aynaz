from django.urls import path

from backend.apps.products.views import IndexPage, ProductListView, ProductDetailView

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('list/product/', ProductListView.as_view(), name='product_list'),
    path('list/product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
