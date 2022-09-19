from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:id>/', views.product_detail, name='product-detail'),
    path('collections/', views.collection_list, name='collection-list'),
    path('collections/<int:id>/', views.collection_detail, name='collection-detail')
]
