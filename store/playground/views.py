from django.shortcuts import render
from django.db.models import Q, F, Value
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from megastore.models import Product, OrderItem, Order, Customer


def play(request):
    result = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, 'playground/play.html', {'result': result})
