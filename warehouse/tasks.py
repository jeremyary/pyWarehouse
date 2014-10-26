from warehouse.models import Order, Classification

from celery import task

import time

@task()
def fulfill_order(order_id=None):
    """ take an order, determine any special classifications (which incur delay for s/g's), and fulfill

    :param order_id: id of order to be fulfilled

    :return: True if successful
    """
    order = Order.objects.get(pk=order_id)
    order.status = 'processing'
    order.save()

    # I want to reflect some delay in the order details UI to make the async tasking a little more obvious
    # let's add 5 seconds for every item in the order and another 30 seconds for each classification
    fulfillment_time = 5 * order.quantity
    fulfillment_time += order.classifications.count()

    time.sleep(fulfillment_time)

    order.status = 'complete'
    order.save()

    return True
