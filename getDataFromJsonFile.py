import json
from datetime import datetime

from klasy.Order import Order
from klasy.Person import Person
from calcExpectedTimeOrders import calcExpectedTimeOrders

def getDataFromJsonFile(sciezka):
    orders = []

    file = open(sciezka,encoding="UTF-8")
    data = json.load(file)

    for item in data["orders"]:

        person = Person(item["name"], item["surname"], item["phoneNumber"], item["email"], item["address"], item["vip"])
        order_ref = item["order"]
        
        receivedTime = datetime.strptime(order_ref["receivedOrderTime"],'%d-%m-%Y %H:%M:%S')
        expectedTime = ""
        if order_ref["expectedDeliveryTime"] != "":
            expectedTime = datetime.strptime(order_ref["expectedDeliveryTime"],'%d-%m-%Y %H:%M:%S')

        order = Order(person, order_ref["pizzaName"], order_ref["size"], receivedTime, expectedTime, order_ref["distance"])
        orders.append(order)

    file.close()

    calcExpectedTimeOrders(orders)

    return orders

