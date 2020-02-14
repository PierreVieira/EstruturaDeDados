from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, element):
        """
        Insere um elemento na pilha
        Complexidade: O(1)
        """
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """
        Remove o elemento do topa da pilha
        Complexidade: O(1)
        """
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node
        raise IndexError("A pilha está vazia")

    def peek(self):
        """
        Retornar o topo da pilha sem remover
        Complexidade: O(1)
        """
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia")

    def __len__(self):
        """Retorna o tamanho da pilha"""
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r += str(pointer.data) + '\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    pilha = Stack()
    pilha.push(3)
    pilha.push('Pierre')
    pilha.push(4.5)
    print(pilha)
    pilha.pop()
    print(pilha)