from django.urls import path

from .views import category_view

app_name = "store"

urlpatterns = [
    path('category/<str:name>', category_view, name="category"),
]
