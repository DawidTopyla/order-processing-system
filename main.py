from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QMainWindow,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout
    )
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from copy import deepcopy
from struktury_danych.my_priority_queue import PriorityQueue
from struktury_danych.my_doubly_linked_list import DoublyLinkedList
from getDataFromJsonFile import getDataFromJsonFile
from exportDataToJsonFile import exportDataToJsonFile

class TitleLabel(QLabel):

    def __init__(self,text):
        super().__init__()
        self.setText(text)
        self.setStyleSheet("""
        font-family: Times New Roman;
        font: bold 15px;
        color: #2F8F9D;
        margin-left: 15px
        """)

class ValueLabel(QLabel):

    def __init__(self,text):
        super().__init__()
        self.setText(text)
        self.setStyleSheet("""
        font-family: Times New Roman;
        font: bold 14px;
        color: #3BACB6;
        margin-left: 15px;
        padding-bottom: 5px;
        border-bottom: 2px solid #82DBD8;
        """)

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ustawienie_poczatkowe()
        panel = QWidget()
        panel.setStyleSheet("""
        background-color: #B3E8E5;
        """)
        self.setCentralWidget(panel)
        layout = QVBoxLayout()

        # Lista zamówień
        self.orders = DoublyLinkedList()

        # Przycisk - wczytywanie zamówień
        self.loadData = QPushButton("WCZYTAJ ZAMÓWIENIA")
        self.loadData.setStyleSheet("""
        QPushButton {
            margin: 10;
            background-color: #3BACB6;
            color: #FFFFFF;
            padding: 10px 20px;
            font: bold 15px;
            border: 2px outset #82DBD8;
            border-radius: 10px;
            }
        """)
        layout.addWidget(self.loadData)

        self.loadData.clicked.connect(self.load)

        # Tytuł
        self.label = QLabel("Zamówienia")
        self.label.setStyleSheet("""
        font-family: Times New Roman;
        font: bold 25px;
        color: #3BACB6;
        """)
        layout.addWidget(self.label,alignment=Qt.AlignCenter)

        # Zdjęcie - zamówienie
        self.img = QLabel(self)
        self.img.setFixedHeight(200)
        self.img.setFixedWidth(300)
        self.img.setStyleSheet("""
        background-color: #c9c1c1;
        border: 5px solid #2F8F9D;
        margin-bottom: 10px
        """)
        layout.addWidget(self.img,alignment=Qt.AlignCenter)

        # Imię i nazwisko - zamówienie
        l_nameAndSurname = TitleLabel("Imię i nazwisko:")
        self.nameAndSurname = ValueLabel("")
        layout.addWidget(l_nameAndSurname)
        layout.addWidget(self.nameAndSurname)

        # Numer telefonu - zamówienie
        l_phoneNumber = TitleLabel("Numer telefonu:")
        self.phoneNumber = ValueLabel("")
        layout.addWidget(l_phoneNumber)
        layout.addWidget(self.phoneNumber)

        # Email - zamówienie
        l_email= TitleLabel("Email:")
        self.email = ValueLabel("")
        layout.addWidget(l_email)
        layout.addWidget(self.email)

        # Adres - zamówienie
        l_address = TitleLabel("Adres:")
        self.address = ValueLabel("")
        layout.addWidget(l_address)
        layout.addWidget(self.address)

        # Zamówiona pizza - zamówienie
        l_pizza = TitleLabel("Zamówiona pizza:")
        self.pizza = ValueLabel("")
        layout.addWidget(l_pizza)
        layout.addWidget(self.pizza)

        # Czas otrzymanego zamówienia - zamówienie
        l_receivedOrderTime = TitleLabel("Złożono zamówienie:")
        self.receivedOrderTime = ValueLabel("")
        layout.addWidget(l_receivedOrderTime)
        layout.addWidget(self.receivedOrderTime)

        # Przewidywany czas zamówienia - zamówienie
        l_expectedDeliveryTime = TitleLabel("Przewidywany czas zamówienia:")
        self.expectedDeliveryTime = ValueLabel("")
        layout.addWidget(l_expectedDeliveryTime)
        layout.addWidget(self.expectedDeliveryTime)

        # Całkowica cena zamówienia - zamówienie
        l_orderPrice = TitleLabel("Cena zamówienia:")
        self.orderPrice = ValueLabel("")
        layout.addWidget(l_orderPrice)
        layout.addWidget(self.orderPrice)


        # Layout dla przycisków "następne" i "poprzednie"
        rowForButtons = QHBoxLayout()

        # Przycisk - przejdź do poprzedniego zamówienia
        self.prev = QPushButton("<- Poprzednie")
        self.prev.setStyleSheet("""
        QPushButton {
            background-color: #3BACB6;
            color: #FFFFFF;
            padding: 5px 10px;
            font: bold 15px;
            border: 2px outset #82DBD8;
            border-radius: 10px;
            }
        :disabled {
            background-color: #6e736f;
        }
        """)
        rowForButtons.addWidget(self.prev)

        self.prev.clicked.connect(self.prev_order)

        # Przycisk - przejdź do następnego zamówienia
        self.next = QPushButton("Następne ->")
        self.next.setStyleSheet("""
        QPushButton {
            background-color: #3BACB6;
            color: #FFFFFF;
            padding: 5px 10px;
            font: bold 15px;
            border: 2px outset #82DBD8;
            border-radius: 10px;
            }
        :disabled {
            background-color: #6e736f;
        }
        """)
        rowForButtons.addWidget(self.next)

        self.next.clicked.connect(self.next_order)

        # Dodanie przycisków do layoutu
        layout.addLayout(rowForButtons)

        # Przycisk - eksportowanie zamówień
        self.exportData = QPushButton("EKSPORTUJ ZAMÓWIENIA")
        self.exportData.setStyleSheet("""
        QPushButton {
            margin: 10;
            background-color: #f23838;
            color: #FFFFFF;
            padding: 10px 20px;
            font: bold 15px;
            border: 2px outset #82DBD8;
            border-radius: 10px;
            }
        """)
        layout.addWidget(self.exportData)

        self.exportData.clicked.connect(self.export)

        
        panel.setLayout(layout)

    def load(self):
        sciezka, _ = QFileDialog.getOpenFileName(self,
                                    "Otwórz plik",".","All files (*.*);;Txt files (*.json)")

        ordersSortedWithPrio = PriorityQueue()
        for order in getDataFromJsonFile(sciezka):
            ordersSortedWithPrio.attach(order,order.expectedDeliveryTime)
        
        while not ordersSortedWithPrio.is_empty():
            order,_ = ordersSortedWithPrio.detach()
            self.orders.insert_before_head(order)

        self.orders.rewind()
        self.setCurrentOrder(self.orders.curr_value())
        self.prev.setDisabled(True)

    def export(self):
        sciezka, _ = QFileDialog.getSaveFileName(self,'Zapisz plik z zamówieniami','.','All files(*);; Text Files(*.json)')
        copyOfOrders = deepcopy(self.orders)
        copyOfOrders.rewind()
        exportDataToJsonFile(sciezka,copyOfOrders)
        
           
    def next_order(self):
        self.orders.move_to_next()
        self.setCurrentOrder(self.orders.curr_value())

        if self.orders.curr_is_tail():
            self.next.setDisabled(True)
        else:
            self.prev.setDisabled(False)

    def prev_order(self):
        self.orders.move_to_back()
        self.setCurrentOrder(self.orders.curr_value())

        if self.orders.curr_is_head():
            self.prev.setDisabled(True)
            self.next.setDisabled(False)
        else:
            self.prev.setDisabled(False)
            self.next.setDisabled(False)

    def setCurrentOrder(self,order):
        self.pixmap = QPixmap("./images/" + order.pizzaName + ".jpg")
        self.img.setScaledContents(True)
        self.img.setPixmap(self.pixmap)

        self.nameAndSurname.setText(order.person.getNameAndSurname()) 
        self.phoneNumber.setText(order.person.phoneNumber) 
        self.email.setText(order.person.email) 
        self.address.setText(order.person.address)
        self.pizza.setText(order.pizzaName + " (" + order.size + ")")
        self.receivedOrderTime.setText(order.receivedOrderTime.strftime("%d/%m/%Y, %H:%M:%S")) 
        self.expectedDeliveryTime.setText(order.expectedDeliveryTime.strftime("%d/%m/%Y, %H:%M:%S")) 
        self.orderPrice.setText(order.price + " zł")


    def ustawienie_poczatkowe(self):
        self.setWindowTitle('SYSTEM OBSŁUGI ZAMÓWIEŃ')
        self.setFixedWidth(350)
        self.setFixedHeight(850)

def main():

    app = QApplication([])
    window = MyWindow()
    window.show()
    
    app.exec()

if __name__ == '__main__':
    main()