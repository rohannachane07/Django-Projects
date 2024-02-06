# sales_app/urls.py
from django.urls import path
from .views import customer_list, product_list, order_list
from .views import product_order_graph

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('products/', product_list, name='product_list'),
    path('orders/', order_list, name='order_list'),
    path('product_order_graph/', product_order_graph, name='product_order_graph'),
]
