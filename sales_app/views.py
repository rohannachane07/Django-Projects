# sales_app/views.py
from django.shortcuts import render
from .models import Customer, Product, Order

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})



from django.http import JsonResponse
from django.db.models import Count  # Import Count from django.db.models

def product_order_graph(request):
    product_orders = Order.objects.values('product__name').annotate(total_orders=Count('id'))
    data = {
        'labels': [entry['product__name'] for entry in product_orders],
        'data': [entry['total_orders'] for entry in product_orders],
    }
    return JsonResponse(data)



