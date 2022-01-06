from django.shortcuts import render
from store.models import Product, Collection
from django.db.models import Q
from django.db.models.aggregates import Count, Max, Min


def say_hello(request):
    queryset = Product.objects.prefetch_related(
        'collection').filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    agg = Product.objects.aggregate(
        count=Count('id'), min_price=Min('unit_price'))

    get_q = Collection.objects.get(id=2)
    print(get_q.title)

    return render(request, 'hello.html', {'name': 'User', 'products': queryset, 'agg': agg, 'get': get_q})
