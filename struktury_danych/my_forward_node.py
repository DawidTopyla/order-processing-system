class ForwardNode:
    
    def __init__(self, value, next):
        self._v = value
        self._n = next
        
    def __str__(self):
        return '[ %r | %s ]' % (self._v, self._n)
        
    
def test_Node_1():
    n1 = ForwardNode(7, None)
    n2 = ForwardNode(12, n1)
    n3 = ForwardNode(-1.5, n2)
    print(n1)
    print(n2)
    print(n3)
    return n3


def test_Node_2():
    x = test_Node_1()
    print(x._v)
    print(x._n._v)
    print(x._n._n._v)
    print(x._n._n._n)
    x._n._n._v = 987
    print(x._n._n._v)
    print(x)


if __name__ == '__main__':
    test_Node_2()