from django.shortcuts import render, get_object_or_404

from warehouse.models import Order, Classification

from warehouse.tasks import fulfill_order

def index(request):
    latest_orders = Order.objects.order_by('-placed')[:3]
    context = {'latest_orders': latest_orders, 'classifications': Classification.objects.all()}
    return render(request, 'warehouse/index.html', context
)
def details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'warehouse/details.html', {'order': order})

def place_order(request):
    classifications = Classification.objects.filter(pk__in=request.POST.getlist('classifications[]'))
    order = Order(item=request.POST['item'], quantity=request.POST['quantity'])
    order.save() #generate pk for mappings and processing
    order.classifications.add(*classifications)

    result = fulfill_order.delay(order.id)
    order.result_id = result.id
    order.save()

    return details(request, order.id)
