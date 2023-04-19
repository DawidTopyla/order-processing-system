from struktury_danych.doublyLinkedNode import DoublyLinkedNode

class DoublyLinkedList:
    
    def __init__(self):
        self._head = None
        self._curr = None
    
    def is_empty(self):
        return self._head == None
    
    def rewind(self):
        self._curr = self._head
        
    def move_to_next(self):
        if self._curr._n is not None:
            self._curr = self._curr._n


    def move_to_back(self):
        if self._curr._p is not None:
            self._curr = self._curr._p
        
    def curr_is_None(self):
        return self._curr._v == None
    
    def curr_is_head(self):
        a = self._head
        b = self._curr
  
        while (a != None and b != None): 
            if (a._v != b._v):
                return False
            a = a._n
            b = b._n
  
        return (a == None and b == None)
    
    def curr_is_tail(self):
        lista = self._head
        while lista._n is not None:
            lista = lista._n
        
        if lista._v == self.curr_value():
            return True
        else:
            return False
    
    def curr_value(self):
        return self._curr._v
    
    def head_value(self):
        return self._head._v
    
    def set_curr_value(self, new_value):
        self._curr._v = new_value
    
    def set_head_value(self, new_value):
        self._head._v = new_value

    
    def insert_after_curr(self, value):
        if self.is_empty():
            self._head=self._curr= DoublyLinkedList(value,None)
        elif self.curr_is_tail():
            self.insert_after_head(value)
        else:
            lista = self._head 
            while lista._v != self._curr._v:
                lista = lista._n

            nextNodes = lista._n
            lista._n = DoublyLinkedList(value,nextNodes)
        
    def insert_after_head(self, value):
        new_node = DoublyLinkedNode(value,None)
         
        if self.is_empty():
            self._head=self._curr = new_node
        else:
            last = self._head
            while (last._n is not None):
                last = last._n
 
            last._n = new_node
            new_node._p = last
        
    def insert_before_head(self, value):
        if self.is_empty():
            new_node = DoublyLinkedNode(value)
            self._head=self._curr = new_node
        else:
            new_node = DoublyLinkedNode(value)
            self._head._p = new_node
            new_node._n = self._head
            self._head = new_node
            
        
        
    def delete_after_curr(self):
        if self.is_empty():
           raise ValueError('pusta lista')
        elif self.curr_is_tail():
            raise ValueError('po current nie ma żadnej wartości')
        else:
            lista = self._head 
            while lista._n._v != self._curr._v:
                lista = lista._n
            
            if lista._n._n is None:
                lista._n = None
            else:
                nextNodes = lista._n._n._n
                lista._n._n = None
                lista._n._n = nextNodes

        
    def delete_after_head(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        else:
            if self._head._n == None:
                self._head = None
            else:
                list = self._head
                while list._n._n is not None:
                    list = list._n
                
                list._n = None
            
        
        
    def delete_head(self):
        if self.is_empty():
            raise ValueError('pusta lista')
        else:
            self._head = None
   


def test():
    list = DoublyLinkedList()
    list.insert_before_head(5)
    list.insert_before_head(3)
    list.insert_before_head(7)
    list.insert_before_head(9)
   
    # list.rewind()
    # print(list._curr)
    # print(list._curr._p)
    # print("UP---------")
    # list.move_to_next()
    # print(list._curr)
    # print(list._curr._p)
    # print("UP---------")
    # list.move_to_next()
    # print(list._curr)
    # print(list._curr._p)
    # print("UP---------")
    # list.move_to_next()
    # print(list._curr)
    # print(list._curr._p)
    # print("DOWN---------")
    list.rewind()
    while not list.curr_is_tail():
        print(list._curr)
        list.move_to_next()

    print(list._curr)
    
if __name__ == '__main__':
    test()
