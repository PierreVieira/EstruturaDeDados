from node import Node


class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def push(self, element):
        """Insere um elemento na fila"""
        node = Node(element)
        if self._last is None:
            self._last = node
        else:
            self._last.next = node
            self._last = node
        if self._first is None:
            self._first = node
        self._size += 1

    def pop(self):
        """Remove o elemento do fim da fila"""
        if self._size > 0:
            element = self._first.data
            self._first = self._first.next
            self._size -= 1
            return element
        raise IndexError("A fila está vazia")

    def peek(self):
        """Retorna o element odo fim da fila"""
        if self._size > 0:
            element = self._first.data
            return element
        raise IndexError("A fila está vazia")

    def __len__(self):
        """Rtorna o tamanho da fila"""
        return self._size

    def __repr__(self):
        if self._size > 0:
            s = ''
            pointer = self._first
            while pointer:
                s += str(pointer.data) + ' '
                pointer = pointer.next
            return s
        return "Fila vazia"

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    fila = Queue()
    for c in range(10):
        fila.push(c)
    print(fila)
    fila.pop()
    print(fila)
    fila.pop()
    print(fila)
