"""Busca binária"""


def binary_search(array, item, begin=0, end=None):
    """
    Utiliza do algoritmo de busca binária para encontrar um ítem em uma lista. Partindo do pressuposto que o array esteja ordenado.
    :param array: lista em que será feita a busca.
    :param item: o ítem que está sendo pesquisado.
    :param begin: posição inicial da busca.
    :param end: posição final da busca.
    :return: posição do ítem caso esse seja encontrado. None caso contrário.
    """
    if end is None:  # Se o end é None, então estamos fazendo a primeira chamada à função
        end = len(array) - 1  # Logo a posição final deve ser o tamanho da lista - 1
    if begin <= end:  # Se a sublista é válida
        m = (begin + end) // 2  # Meio da lista
        if array[m] == item:  # Se o meio da lista é o elemento que estamos pesquisando
            return m
        if item < array[m]:  # Se o ítem pesquisado for menor que o ítem que está no meio da lista
            return binary_search(array, item, begin, m - 1)  # Faça a pesquisa pela esquerda
        return binary_search(array, item, m + 1, end)  # Senão, quer dizer que ele está a direita da lista
    return None  # Caso o elemento não esteja na lista retorne None


if __name__ == '__main__':
    lista = [i/5 for i in range(10000000)]
    busca = [1, 87, 93812, 90000, 12, 15, -3, 0, -1, 90, 12222]
    for b in busca:
        indice = binary_search(lista, b)
        if indice is not None:
            print(f'O elemento {b} está na posição {indice}')
        else:
            print(f'O elemento {b} não está na lista.')
