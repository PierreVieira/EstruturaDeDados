from node import Node


class LinkedList:
    """Sequência de nós (um ligado a outro) de tal forma que um nó saiba qual será o nó seguinte"""

    def __init__(self):
        self.head = None  # Referência para o primeiro nó
        self._size = 0  # Tamanho da lista encadead

    def append(self, element):
        """
        Insere um elemento no final da lista.
        Complexidade: O(n)
        :param element: elemento a ser inserido
        :return: None
        """
        no = Node(element)
        if self.head:  # Quer dizer que já tem um elemento na cabeça
            pointer = self.head
            while pointer.next:  # Enquanto o ponteiro for diferente de None (significa que não chegamos ao fim)
                pointer = pointer.next  # Andando com o ponteiro
            pointer.next = no
        else:  # Quer dizer que não tem um elemento na cabeça, estamos inserindo o primeiro elemento na lista
            self.head = no  # Primeira inserção
        self._size += 1  # O tamanho da lista aumenta após a inserção do elemento

    def __len__(self):
        """
        :return: tamanho da lista
        """
        return self._size

    # Sobrecarga de operador
    def __getitem__(self, index):
        """
        Complexidade: O(n)
        :param index: índice do elemento a ser pesquisado
        :return: elemento que está no índice informado
        """
        # a = lista[6]
        pointer = self.head
        for i in range(index):
            if pointer:  # Pointer not is none
                pointer = pointer.next
            else:  # Deve-se lançar um erro
                raise IndexError("O índice não está disponível para a lista")
        if pointer:
            return pointer.data
        raise IndexError("O índice não está disponível para a lista")

    # Sobrecarga de operador
    def __setitem__(self, index, value):
        """
        Complexidade: O(n)
        :param index: índice do elemento a ser alterado
        :param value: novo valor que ficará no índice informado
        :return: None
        """
        # lista[5] = 9
        pointer = self.head
        for i in range(index):
            if pointer:  # Pointer not is none
                pointer = pointer.next
            else:  # Deve-se lançar um erro
                raise IndexError("O índice não está disponível para a lista")
        if pointer:
            pointer.data = value
        else:
            raise IndexError("O índice não está disponível para a lista")

    def index(self, element):
        """
        :param element: elemento a ser pesquisado
        :return: índice do elemento na lista
        """
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'O elemento {element} não está na lista')


if __name__ == '__main__':
    lista = LinkedList()
    lista.append(8)
    lista.append('pierre')
    print(lista[1])
    print(len(lista))
    print(lista.index(8))