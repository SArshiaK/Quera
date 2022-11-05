from .models import OrderItem, Order
# from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponseNotFound


def checkout(request, order_pk):
    try:
        order = Order.objects.get(pk=order_pk)
    except Order.DoesNotExist:
        return HttpResponseNotFound("404")
    orderitems = OrderItem.objects.all()
    totalPrice = 0
    for i in range(len(orderitems)):
        # orderitem = OrderItem.objects.get(pk=order_pk)
        if orderitems[i].order == order:
            first_product = orderitems[i].product
            quantity = orderitems[i].quantity

            price_in_dec = first_product.price
            # price_in_dec = 9999999.12945678910238948242914
    
            totalPrice += price_in_dec * quantity
    strP = str(totalPrice)
    
    dot_index = strP.find('.')
    if dot_index != -1 :
        strP = strP[:dot_index+3]
    

    # orderitems = OrderItem.objects.all()
    # return JsonResponse({'total_price': orderitems[0].quantity})
    return JsonResponse({'total_price':strP})
    
    # return HttpResponseNotFound("404") 