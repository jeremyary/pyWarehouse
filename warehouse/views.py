from django.shortcuts import render, get_object_or_404

from warehouse.models import Order
from warehouse.models import Classification

def index(request):
    latest_orders = Order.objects.order_by('-placed')[:3]
    context = {'latest_orders': latest_orders, 'classifications': Classification.objects.all()}
    return render(request, 'warehouse/index.html', context)

def details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'warehouse/details.html', {'order': order})

def place_order(request):
    classifications = Classification.objects.filter(pk__in=request.POST.getlist('classifications[]'))
    order = Order(item=request.POST['item'], quantity=request.POST['quantity'])
    order.save()
    order.classifications.add(*classifications)
    return details(request, order.id)
