from datetime import datetime,timedelta
from math import ceil

timeOfStartMakingOrders = datetime.strptime('08-05-2023 8:00:00','%d-%m-%Y %H:%M:%S')

def calcExpectedTimeOrders(orders):
    orders.sort(key=lambda x: x.receivedOrderTime)
    ordersFromYesterday = []
    
    for order in orders:
        if order.receivedOrderTime < timeOfStartMakingOrders:
            ordersFromYesterday.append(order)


    for order in orders:
        if order.receivedOrderTime < timeOfStartMakingOrders:
            continue
        
        # Czas przygotowania zamówienia
        preparationTime = 30
        # Czas ukończenia przygotowania zamówienia
        finishedPreparationTime = order.receivedOrderTime + timedelta(minutes=preparationTime)
        # Czas dostawy (1km = 2min)
        deliveryTime =  ceil(order.distance) * 2
        # Łączny czas
        fullDeliveryTime = preparationTime + deliveryTime

        expectedDeliveryTime = order.receivedOrderTime + timedelta(minutes=fullDeliveryTime)
        
        while len(ordersFromYesterday) != 0:
            if finishedPreparationTime > ordersFromYesterday[0].expectedDeliveryTime:
                if order.receivedOrderTime > ordersFromYesterday[0].expectedDeliveryTime:
                    ordersFromYesterday.pop(0)
                    break
                else:
                    expectedDeliveryTime = ordersFromYesterday[0].expectedDeliveryTime + timedelta(minutes=fullDeliveryTime)
                    ordersFromYesterday.pop(0)
                    break
            else:
                break
        
        order.expectedDeliveryTime = expectedDeliveryTime