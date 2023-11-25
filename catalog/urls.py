from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, product

app_name = CatalogConfig.name
urlpatterns = [
    path('', index),
    path('contacts/', contact),
    path('product/<int:pk>/', product, name='product')
]