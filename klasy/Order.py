from utils import getPriceOfPizza

class Order:
    def __init__(self, person, pizzaName, size, receivedOrderTime, expectedDeliveryTime, distance):
        self.person=person
        self._pizzaName=pizzaName
        self._size=size
        self._receivedOrderTime=receivedOrderTime
        self._expectedDeliveryTime=expectedDeliveryTime
        self._distance=distance
        self._price=self.calcPrice()


    @property
    def pizzaName(self):
        return self._pizzaName

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,cena):
        self._price=cena

    @property
    def receivedOrderTime(self):
        return self._receivedOrderTime

    @property
    def expectedDeliveryTime(self):
        return self._expectedDeliveryTime

    @expectedDeliveryTime.setter
    def expectedDeliveryTime(self,time):
        self._expectedDeliveryTime=time

    @property
    def distance(self):
        return self._distance

    def calcPrice(self):
        extraPriceForDistance = self._distance * 0.5
        priceOrder = getPriceOfPizza(self._pizzaName, self._size) + extraPriceForDistance
        if self.person.vip:
            priceOrder = priceOrder - (priceOrder*(1/10))

        return '{0:.2f}'.format(priceOrder)