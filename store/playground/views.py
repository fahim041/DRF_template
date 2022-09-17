from django.shortcuts import render
from django.db.models import Q, F
from megastore.models import Product, OrderItem, Order


def play(request):
    queryset = Order.objects.prefetch_related(
        'orderitem_set').order_by('-placed_at')[:5]
    return render(request, 'playground/play.html', {'products': list(queryset)})
