class _Node:
    def __init__(self, data = None,prev = None, next = None):
        self._data = data
        self._prev = prev
        self._next = next
        self._last = None
        self.it = None

    #def __eq__(self, other):
       # return self._data == other._data

    def __lt__(self, other):
        return self._data < other._data

    def __gt__(self, other):
        return self._data > other._data

class MyList:

    def __init__(self):
        self._list = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def append(self, x):
        node = _Node(x)

        if self.is_empty():
            self._list = node
            self._last = node
        else:
            last_node = self._last
            last_node._next = node
            node._prev = last_node
            self._last = node
        self._size += 1

    def __iter__(self):
        return self

    def index(self,x,start = None,stop = None):
        """Restituisce l’indice del primo elemento della lista il cui valore è x.
        L’assenza di tale elemento produce un errore. """

        if self.is_empty():
            raise ValueError
        else:

            i = 0
            for data in self.generator():
                if data == x:
                    return i
                i += 1
            raise ValueError

    def generator(self):
        if not self.is_empty():
            temp = self._list
            for _ in range(self._size):
                yield temp._data
                if(temp._next == None):
                    break
                else:
                    temp = temp._next

    def __len__(self):
        return self._size

    def stampa_lista(self):
        for data in self.generator():
            print(data)



