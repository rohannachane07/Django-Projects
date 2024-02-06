# sales_app/admin.py
# sales_app/admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Customer, Product, Order
from .resources import CustomerResource, ProductResource, OrderResource

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource


