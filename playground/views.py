from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, OrderItem

# Create your views here.


def say_hello(request):
    queryset = OrderItem.objects.filter(product_id__collection__id=3)

    return render(request, 'hello.html', {'fname': 'Naruto', 'lname': 'Uzumaki', 'products': list(queryset)})
