def busca_linear(lista, elemento):
    """
    Complexidade -> O(n)
    :param lista: Onde será feita a busca.
    :param elemento: elemento a ser buscado.
    :return: índice do elemento caso ele esteja na lista, None caso contrário.
    """
    for c in range(len(lista)):
        if lista[c] == elemento:
            return c
    return None


"""
Essa maneira não é a mais eficiente para realizar a busca. Caso os elementos estejam ordenados, o mais aconselhável é
utilizar o algoritmo de busca binária (complexidade O(log(n)).
"""
if __name__ == '__main__':
    lista = [i+1 for i in range(10)]
    print(busca_linear(lista, 6))
