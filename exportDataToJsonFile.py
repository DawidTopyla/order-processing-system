import json

def exportDataToJsonFile(sciezka,orders): 
    with open(sciezka,'w',encoding="UTF-8") as exportOrders:
        jsonObject = {"orders": []}

        while not orders.curr_is_tail():
            curr = orders.curr_value()
            order = createNewOrder(curr.person.name,
            curr.person.surname,
            curr.person.phoneNumber,
            curr.person.email,
            curr.person.address,
            curr.person.vip,
            curr.pizzaName,
            curr.size,
            curr.receivedOrderTime.strftime("%d-%m-%Y, %H:%M:%S"),
            curr.expectedDeliveryTime.strftime("%d-%m-%Y, %H:%M:%S"),
            curr.distance,
            curr.price,
            )
            jsonObject["orders"].append(order)

            orders.move_to_next()

        last = orders.curr_value()
        lastOrder = createNewOrder(last.person.name,
            last.person.surname,
            last.person.phoneNumber,
            last.person.email,
            last.person.address,
            last.person.vip,
            last.pizzaName,
            last.size,
            last.receivedOrderTime.strftime("%d-%m-%Y, %H:%M:%S"),
            last.expectedDeliveryTime.strftime("%d-%m-%Y, %H:%M:%S"),
            last.distance,
            last.price,
            )
        jsonObject["orders"].append(lastOrder)
        print(json.dumps(jsonObject, indent=2,ensure_ascii=False),file=exportOrders)

def createNewOrder(name,surname,phoneNumber,email,address,vip,pizzaName,size,receivedOrderTime,expectedDeliveryTime,distance,price):
    newObject = {}
    newObject["name"] = name
    newObject["surname"] = surname
    newObject["phoneNumber"] = phoneNumber
    newObject["email"] = email
    newObject["address"] = address
    newObject["vip"] = vip

    newOrder = {}
    newOrder["pizzaName"] = pizzaName
    newOrder["size"] = size
    newOrder["receivedOrderTime"] = receivedOrderTime
    newOrder["expectedDeliveryTime"] = expectedDeliveryTime
    newOrder["distance"] = distance
    newOrder["price"] = price

    newObject["order"] = newOrder

    return newObject






     
