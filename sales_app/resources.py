# sales_app/resources.py
from import_export import resources
from .models import Customer, Product, Order

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
