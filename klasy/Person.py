class Person:
    def __init__(self, name, surname, phoneNumber, email,address, vip):
        self._name=name
        self._surname=surname
        self._phoneNumber=phoneNumber
        self._email=email
        self._address=address
        self._vip=vip

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @property
    def email(self):
        return self._email

    @property
    def address(self):
        return self._address

    @property
    def vip(self):
        return self._vip


    def getNameAndSurname(self):
        return self._name+" "+self._surname
