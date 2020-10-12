"""
Considerações:
Nesse programa estou evitando usar as funções prontas do python como len() que retorna o tamanho, set() que retorna
o conjunto de elementos não repetidos do iterável (nesse caso a lista) e até mesmo a plavra reservada 'in' justamente
para mostrar como esses códigos são implementados por debaixo dos panos e consequentemente tendo uma visão melhor de
sua complexidade assintótica.

Para as análises de complexidade estamos considerando o pior caso.
"""


def tamanho(lista):
    """
    :return: Tamanho da lista
    Complexidade: O(n)
    """
    cont = 0
    for _ in lista:  # Executa n vezes
        cont += 1
    return cont


def busca_binaria(lista, valor, inicio=0, fim=None):
    """
    Complexidade para o pior caso: O(log(n))
    :param lista: lista que irá ser feita a busca binária
    :param valor: valor a ser pesquisado na lista
    :param inicio: valor da posição esquerda na recursão atual (opcional)
    :param fim: valor da posição direita na recursão atual (opcional)
    :return: True se o valor está na lista, False caso contrário
    """
    if fim is None:  # Se o fim é None, então estamos fazendo a primeira chamada à função
        fim = len(lista) - 1  # Logo a posição final deve ser o tamanho da lista - 1
    if inicio <= fim:  # Se a sublista é válida
        m = (inicio + fim) // 2  # Meio da lista
        if lista[m] == valor:  # Se o meio da lista é o elemento que estamos pesquisando
            return True
        if valor < lista[m]:  # Se o ítem pesquisado for menor que o ítem que está no meio da lista
            return busca_binaria(lista, valor, inicio, m - 1)  # Faça a pesquisa pela esquerda
        return busca_binaria(lista, valor, m + 1, fim)  # Senão, quer dizer que ele está a direita da lista
    return False  # Caso o elemento não esteja na lista retorne False


def remove_repetidos(lista):
    """
    Complexidade para o pior caso: O(n*log(n))
    :param lista: lista a ser removido os repetidos
    :return: a lista sem os elementos repetidos
    """
    sem_repetidos = []
    for valor in lista:  # Executa n vezes
        if not busca_binaria(sem_repetidos, valor):  # Executa log(n) vezes (log na base 2)
            sem_repetidos.append(valor)
    return sem_repetidos


def quicksort(lista):
    """
    Complexidade: O(n*log(n)) [estou desconsiderando o pior caso O(n²) que é extremamente raro]
    :param lista: lista a ser ordenada
    :return: lista ordenada
    """
    if tamanho(lista) <= 1:
        return lista

    pivot = lista[0]
    equal = [x for x in lista if x == pivot]
    menor = [x for x in lista if x < pivot]
    maior = [x for x in lista if x > pivot]
    return quicksort(menor) + equal + quicksort(maior)


def forca_bruta(lista):
    """
    Complexidade para o pior caso: O(n²) [O de n ao quadrado]
    A ideia aqui é fazer o algoritmo mais lento possível.
    :return: True quando os valores da lista são únicos, false caso contrário.
    """
    tamanho_lista = tamanho(lista)
    for i in range(tamanho_lista):  # Executa n vezes
        cont = 0
        for j in range(tamanho_lista):  # Executa n vezes
            if lista[i] == lista[j]:
                cont += 1
        if cont > 1:
            return False  # Os valores não são únicos
    return True  # Os valores são únicos


def n_log_n(lista):
    """
    Complexidade para o pior caso: O(n*log(n))
    :return: True quando os valores da lista são únicos, false caso contrário.
    """
    lista_ordenada = quicksort(lista)  # Complexidade O(n*log(n))
    lista_sem_repetidos = remove_repetidos(lista_ordenada)  # Complexidade O(n*log(n))
    tamanho1 = tamanho(lista)  # Complexidade O(n)
    tamanho2 = tamanho(lista_sem_repetidos)  # Complexidade O(n)
    return tamanho1 == tamanho2  # Complexidade O(1)


def lista_ordenada(lista):
    """
    Complexidade para o pior caso: O(n)
    :param lista: lista que iremos verificar se é ou não ordenada
    :return: True se a lista for ordenada, False caso contrário
    """
    for i in range(tamanho(lista) - 1):
        if lista[i] < lista[i + 1]:
            return False
    return True


def linear(lista):
    """
    Complexidade para o pior caso: O(n)
    tabelas hash ou mapas hash permvalor associação de elementos em O(1). Para cada elemento da lista, aloque-os no mapa.
    Se o elemento já existir, retorne FALSE. Caso consiga percorrer toda a lista, retorne TRUE.
    :return: True quando os valores da lista são únicos, false caso contrário.
    """
    hash = set()
    for n in lista:
        if n in hash:
            return False
        hash.add(n)
    return True


if __name__ == '__main__':
    lista_teste = [32, 1, 22, 10, 21, 14, 1, 69, 12, 11, 19, 3]
    print(forca_bruta(lista_teste))
    print(n_log_n(lista_teste))
    print(linear(lista_teste))
