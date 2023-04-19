from struktury_danych.my_forward_node import ForwardNode

class DoublyLinkedNode(ForwardNode):
    
    def __init__(self, value, next=None, prev=None):
        super().__init__(value, next)
        self._p = prev
