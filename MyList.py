"""Da Fare:
    Commenti, Documentazione, Eccezioni, Iteratore nel costruttore"""
class _Node():
    def __init__(self, data = None):
        self._data = data
        self._previous = None
        self._next = None

    def __str__(self):
        if isinstance(self._data, str):
            return "'" + self._data + "'"
        return str(self._data)

    def __le__(self, other):
        if type(self) != type(other):
            raise TypeError
        return self._data <= other._data

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError
        return self._data < other._data

    def __gt__(self, other):
        if type(self) != type(other):
            raise TypeError
        return self._data > other._data

    def __ge__(self, other):
        if type(self) != type(other):
            raise TypeError
        return self._data >= other._data

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self._data == other._data

    def __ne__(self, other):
        if type(self) != type(other):
            return True
        return self._data != other._data

class MyList():

    def __init__(self):
        self._list = None
        self._last = None
        self._size = 0


    def __add__(self, other):
        if isinstance(other, MyList):
            list = MyList()
            list.extend(self)
            list.extend(other)
            return list
        else:
            raise TypeError

    def __iadd__(self, other):
        if isinstance(other, MyList):
            self.extend(other)
            return self
        else:
            raise TypeError

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __bool__(self):
        return self._size > 0

    def __str__(self):
        if self._size == 0:
            return "[]"
        temp = self._list
        string = "[" + str(temp)
        for _ in range(self._size - 1):
            temp = temp._next
            string += ", " + str(temp)
        string += "]"
        return string

    def __iter__(self):
        temp = self._list
        for _ in range(self._size):
            yield temp._data
            temp = temp._next

    def __le__(self, other):
        if type(self) != type(other):
            raise TypeError
        while (self._list != None) & (other._list != None):
            if self._list._data == other._list._data:
                self._list = self._list._next
                other._list = other._list._next
            else:
                return self._list._data <= other._list._data
        if other._list != None:
            return True
        return False

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError
        while (self._list != None) & (other._list != None):
            if self._list._data == other._list._data:
                self._list = self._list._next
                other._list = other._list._next
            else:
                return self._list._data < other._list._data
        if len(self) >= len(other):
            return False

    def __ge__(self, other):
        if type(self) != type(other):
            raise TypeError
        while (self._list != None) & (other._list != None):
            if self._list._data == other._list._data:
                self._list = self._list._next
                other._list = other._list._next
            else:
                return self._list._data >= other._list._data
        if self._list != None:
            return True
        return False

    def __gt__(self, other):
        if type(self) != type(other):
            raise TypeError
        while (self._list != None) & (other._list != None):
            if self._list._data == other._list._data:
                self._list = self._list._next
                other._list = other._list._next
            else:
                return self._list._data > other._list._data
        if len(self) > len(other):
            return True

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        while (self._list != None) & (other._list != None):
            if self._list._data == other._list._data:
                self._list = self._list._next
                other._list = other._list._next
            else:
                return False
        if len(self) == len(other):
            return True
        return False

    def __ne__(self, other):
        if type(self) != type(other):
            return True
        while (self._list != None) & (other._list != None):
            if self._list._data == other._list._data:
                self._list = self._list._next
                other._list = other._list._next
            else:
                return True
        if len(self) != len(other):
            return True
        return False

    def append(self, x):
        new_node = _Node(x)
        if self.is_empty():
            self._list = new_node
            self._last = new_node
        else:
            self._last._next = new_node
            new_node._previous = self._last
            self._last = new_node
        self._size += 1

    def insert(self, i, x):
        if -self._size < i < 0:
            i += self._size
        elif i < -self._size:
            i = 0
        elif i >= self._size:
            i = self._size
        new_node = _Node(x)
        if i == 0:
            new_node._next = self._list
            if not (self.is_empty()):
                self._list._previous = new_node
            self._list = new_node

        elif i < self._size:
            prev = self._get_node(i-1)
            next = self._get_node(i)
            prev._next = new_node
            new_node._previous = prev
            next._previous = new_node
            new_node._next = next

        elif i == self._size:
            prev = self._last
            prev._next = new_node
            new_node._previous = prev
            self._last = new_node
        self._size += 1

    def _get_node(self, i):
        """Restituisce il nodo all'indice i"""
        temp = self._list
        for _ in range(i):
            temp = temp._next
        return temp

    def count(self, x):
        return self._size

    def copy(self):
        new_list = MyList()
        list_iter = self.__iter__()
        for i in range(self._size):
            new_data = next(list_iter)
            new_list.append(new_data)
        return new_list

    def clear(self):
        self._list = None
        self._size = 0

    def remove(self, x):
        if self.is_empty():
            raise Exception
        index = self._search(x)
        if index == None:
            raise Exception
        else:
            if self._size == 1:
                self._list = None
            elif index == 0:
                node = self._get_node(1)
                node._previous = None
                self._list = node
            elif index == self._size - 1:
                node = self._get_node(index - 1)
                node._next = None
            else:
                prev = self._get_node(index - 1)
                next = self._get_node(index + 1)

                prev._next = next
                next._previous = prev
            self._size -= 1

    def _search(self, x):
        """Ritorna l'indice dell'elemento x ricercato"""
        list_iter = self.__iter__()
        for i in range(self._size):
            new_data = next(list_iter)
            if new_data == x:
                return i
        return None

    def reverse(self):
        if self._size >= 2:
            first = self._list
            last = self._get_node(self._size-1)
            for i in range(int(self._size/2)):
                self.swapNodes(first, last)
                first = first._next
                last = last._previous

    def swapNodes(self, first, last):
        temp = first._data
        first._data = last._data
        last._data = temp


    def pop(self, i = None):
        if -self._size < i < 0:
            i += self._size
        if self.is_empty():
            raise Exception
        elif i < 0 or i > self._size:
            raise Exception
        else:
            index_node = self._get_node(i)
            if self._size == 1:
                self._list = None
            elif i == 0:
                node = self._get_node(1)
                node._previous = None
                self._list = node
            elif i == self._size - 1:
                node = self._get_node(i - 1)
                node._next = None
            else:
                prev = self._get_node(i - 1)
                next = self._get_node(i + 1)
                prev._next = next
                next._previous = prev
            self._size -= 1
            return index_node._data

    def extend(self, iterable):
        if isinstance(iterable, MyList):
            if not iterable.is_empty():
                copy = iterable.copy()
                if self.is_empty():

                    self._list = copy._list
                    self._size = copy._size
                    self._last = copy._last
                else:
                    last = self._last
                    last._next = copy._list
                    self._size += copy._size
                    copy._list._previous = last
                    self._last = copy._last
        else:
            try:
                it = iter(iterable)
                while True:
                    try:
                        self.append(next(it))
                    except Exception as e:
                        break
            except Exception:
                raise TypeError

    def index(self, x, start = None, end = None):
        if start == None and end == None:
            index = self._search(x)
            if index == None:
                raise ValueError
            return index
        elif start < 0 or start >= self._size or end < 0 or end >= self._size:
            raise Exception
        elif start != None:
            temp = self._list
            for i in range(start):
                temp = temp._next
            if end == None:
                for i in range(self._size - start):
                    if temp._data == x:
                        return i + start
                    temp = temp._next
                raise ValueError
            elif end != None:
                for i in range(end - start + 1):
                    if temp._data == x:
                        return i + start
                    temp = temp._next
                raise ValueError

    def sort(self, key=None, reverse = False):
        if self.is_empty() or self._size == 1:
            return
        else:
            first = self._list
            for i in range(self._size-1):
                temp = first
                for j in range(self._size - i - 1):
                        if temp > temp._next:
                            if not reverse:
                                self._swap_data(temp, temp._next)
                        elif temp < temp._next:
                            if reverse:
                                self._swap_data(temp, temp._next)
                        temp = temp._next

    def _swap_data(self, a, b):
        tmp = a._data
        a._data = b._data
        b._data = tmp

    def __del__(self):
        del self

    def __contains__(self, item):
        list_iter = self.__iter__()
        for i in range(self._size):
            new_data = next(list_iter)
            if new_data == item:
                return True
        return False

    def __getitem__(self, item):

        if isinstance(item, int):
            if -self._size < item < 0:
                item += self._size
            if item < 0 or item >= self._size:
                raise IndexError
            node = self._get_node(item)
            return self._get_node(item)._data

        elif isinstance(item, slice):
            start = 0
            size = self._size
            stop = size
            step = 1
            if item.step != None:
                if item.step == 0:
                    raise ValueError
                else:
                    step = item.step
                if item.step < 0:
                    start = size - 1
                    stop = -1
            if item.start != None:
                start = item.start
                if start < 0:
                    start += size
                if start < 0:
                    start = 0
                    if step < 0:
                        start = -1
                elif start >= size:
                    start = size
                    if step < 0:
                        start = size - 1
            if item.stop != None:
                stop = item.stop
                if stop < 0:
                    stop += size
                if stop < 0:
                    stop = -1
                elif stop >= size:
                    stop = size
            new_list = MyList()
            if (step > 0 and start > stop) or (step < 0 and start < stop):
                pass
            elif step > 0:
                temp = self._list
                index = 0
                quantity = int((stop - start) / step)
                if ((stop - start) % step) != 0:
                    quantity += 1
                for _ in range(start):
                    temp = temp._next
                index += start
                for _ in range(quantity):
                    new_list.append(temp._data)
                    if (index + step < stop):
                        for _ in range(step):
                            temp = temp._next
                        index += step
            elif step < 0:
                temp = self._last
                index = size
                quantity = int((start - stop) / abs(step))
                if ((start - stop) % abs(step)) > 0:
                    quantity += 1
                for _ in range(size - 1 - start):
                    temp = temp._previous
                index -= size - 1 - start
                for _ in range(quantity):
                    new_list.append(temp._data)
                    if (index + step > stop):
                        for _ in range(abs(step)):
                            temp = temp._previous
                        index += step
            return new_list
        else:
            raise TypeError

    def __setitem__(self, item, x):

        if isinstance(item, int):
            if -self._size < item < 0:
                item += self._size
            if item < 0 or item >= self._size:
                raise IndexError
            node = self._get_node(item)

            node._data = x
            return

        elif isinstance(item, slice):
            start = 0
            size = self._size
            stop = size
            step = 1

            if item.step != None:
                if item.step == 0:
                    raise ValueError
                else:
                    step = item.step
                if item.step < 0:
                    start = size - 1
                    stop = -1

            if item.start != None:
                start = item.start
                if start < 0:
                    start += size
                if start < 0:
                    start = 0
                    if step < 0:
                        start = -1
                elif start >= size:
                    start = size
                    if step < 0:
                        start = size - 1 # start
            if item.stop != None:
                stop = item.stop
                if stop < 0:
                    stop += size
                if stop < 0:
                    stop = -1
                elif stop >= size:
                    stop = size
            #Inizializzo lista
            new_list = MyList()

            if (step > 0 and start > stop) or (step < 0 and start < stop):
                pass

            elif step > 0:
                temp = self._list
                index = 0
                quantity = int((stop - start) / step)

                if ((stop - start) % step) != 0:
                    quantity += 1
                print(quantity,len(x))

                if step != 1:
                    if quantity == len(x):
                        for _ in range(start):
                            temp = temp._next
                        index += start
                        for i in range(quantity):
                            temp._data = x[i]
                            if (index + step < stop):
                                for _ in range(step):
                                    temp = temp._next
                                index += step
                    else:
                        raise  ValueError

                else:
                    for _ in range(start):
                        temp = temp._next

                    index = quantity if quantity < len(x) else len(x)

                    for i in range(index):
                        print(i)
                        temp._data = x[i]
                        temp = temp._next


                    next = temp
                    remain = len(x) - quantity
                    print("Remain " + str(remain))
                    temp.next = x[quantity - 1]
                    self._size += remain
                    x._last._next = next



                    #LOLOL

            elif step < 0:
                temp = self._last
                index = size
                quantity = int((start - stop) / abs(step))
                if ((start - stop) % abs(step)) > 0:
                    quantity += 1
                for _ in range(size - 1 - start):
                    temp = temp._previous
                index -= size - 1 - start
                for _ in range(quantity):
                    new_list.append(temp._data)
                    if (index + step > stop):
                        for _ in range(abs(step)):
                            temp = temp._previous
                        index += step
            return new_list
            """
            if node == self._last:
                node._data = item
                return
            elif node == self._list:
                node._data = item
                return
            else:
                next = node._next
                prev = node._previous"""


    def _list_compare(self, list):
        list_len = len(list)
        if list_len != self._size :
            return 0
        else:
            return self._compare(list)

    def _compare(self, list):
        it = iter(self)
        for i in list:
            if i != next(it):
                return 0
        return 1