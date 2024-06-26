# System obsługi zamówień

## Cel
Stworzenie programu wykorzystującego jedną ze struktur poznanych na przedmiocie **Algorytmy i strukury danych.**
W projekcie wykorzystano jezyk Python, moduł datetime oraz bibliotekę PyQt5 w celu stworzenia prostego GUI.

## Budowa 
Prace podzielono na  foldery:
  * images - przechowywujące obrazy dla pizzy
  * klasy - zawiera klasy [Order](https://github.com/DawidTopyla/order-processing-system/blob/main/klasy/Order.py) i [Person](https://github.com/DawidTopyla/order-processing-system/blob/main/klasy/Person.py) wykorzystane do tworzenia zamówień
  * struktury danych - tutaj przechowywane są użyte strukury

Oraz pliki:

### [calcExpectedTimeOrders.py](https://github.com/DawidTopyla/order-processing-system/blob/main/calcExpectedTimeOrders.py)
Funkcja przyjmuje zamówinie i oblicza oczekiwany czas dostawy.

### [getDataFromJsonFile.py](https://github.com/DawidTopyla/order-processing-system/blob/main/getDataFromJsonFile.py)
Funkcja pobiera dane z pliku .json i tworzy obiekty klasy **Person** i **Orders**.
Zwraca zamówienia.

### [exportDataToJsonFile.py](https://github.com/DawidTopyla/order-processing-system/blob/main/exportDataToJsonFile.py)
Program ma dwie fukcje, które sortują i tworzą nowy plik .json zawierający informacje końcowe o zamówieniach.

### [utils.py](https://github.com/DawidTopyla/order-processing-system/blob/main/utils.py)
Zawiera obiekt Json przechowywujący informacje o pizzy, jej rozmiarze i cenie.

### [main.py](https://github.com/DawidTopyla/order-processing-system/blob/main/main.py)
Główy plik w projekcie. W nim tworzone jest okno widoczne dla użytkownika.
Wykorzystuje [DoublyLinkedList](https://github.com/DawidTopyla/order-processing-system/blob/main/struktury_danych/my_doubly_linked_list.py) do przechowywania zamówień. Jej metody wykorzystano przy przechodzeniu pomiędzy zamówieniami.
[PriorityQueue](https://github.com/DawidTopyla/order-processing-system/blob/main/struktury_danych/my_priority_queue.py) użyto w celu sortowania zamówień po oczekiwanym czasie dostawy.

## Przykłady graficzne projektu

| Widok początkowy | Widok po wczytaniu danych |
|:---:|:---:|
| ![Widok 1](https://github.com/DawidTopyla/order-processing-system/blob/main/assets/system1.png)  | ![Widok 2](https://github.com/DawidTopyla/order-processing-system/blob/main/assets/system2.png) |

