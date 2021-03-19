from django.urls import path

from .views import ProductListView

app_name = "store"

urlpatterns = [
    path('products', ProductListView.as_view(), name="products")
]
