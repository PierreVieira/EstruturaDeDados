class Node:
    """Um nó contém espaço para armazenar o dado e espaço para armazenar a posição do nó seguinte"""
    def __init__(self, data):
        self.data = data  # Dado a ser armazenado
        self.next = None  # Guarda a posição do nó seguinte


if __name__ == '__main__':
    no1 = Node(5)
    no2 = Node(9)
    no1.next = no2
    print(no1.next.data)
