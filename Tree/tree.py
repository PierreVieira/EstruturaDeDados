from random import sample, seed


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Referência para o nó à esquerda
        self.right = None  # Referência para o nó à direita

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None, node=None):
        self._posfixo = ''
        self._infixo = ''
        self._prefixo = ''
        if node:
            self.root = node
        elif data:  # se o usuário especificou o nó
            node = TreeNode(data)
            self.root = node  # Raiz da árvore
        else:
            self.root = None

    @property
    def prefixo(self):
        self._preorder_traversal()
        return self._prefixo[:-1]

    @property
    def infixo(self):
        self._inorder_traversal()
        return self._infixo[:-1]

    @property
    def posfixo(self):
        self._postorder_traversal()
        return self._posfixo[:-1]

    def _preorder_traversal(self, node=None):
        """Faz o percurso na árvore em pós ordem"""
        if node is None:  # se o nó é vazio
            node = self.root  # o nó é a raíz da arvore
        self._prefixo += node.__str__() + ' '
        if node.left:  # se tem filho à esquerda
            self._preorder_traversal(node.left)
        if node.right:  # se tem filho à direita
            self._preorder_traversal(node.right)

    def _inorder_traversal(self, node=None):
        """Percurso em ordem simétrica"""
        if node is None:  # se o nó é vazio
            node = self.root
        if node.left:
            self._inorder_traversal(node.left)
        self._infixo += node.__str__() + ' '
        if node.right:
            self._inorder_traversal(node.right)
        # A subarvore da direita só será exibida quando a subarvore da esquerda for exibida

    def _postorder_traversal(self, node=None):
        """Faz o percurso na árvore em pós ordem"""
        if node is None:  # se o nó é vazio
            node = self.root  # o nó é a raíz da arvore
        if node.left:  # se tem filho à esquerda
            self._postorder_traversal(node.left)
        if node.right:  # se tem filho à direita
            self._postorder_traversal(node.right)
        self._posfixo += node.__str__() + ' '

    def height(self, node=None):
        """Retorna o tamanho da árvore"""
        if node is None:  # se o nó é vazio
            node = self.root  # o nó é a raíz arvore
        # inicialização das variáveis de cálculo de altura
        hleft = 0
        hright = 0
        if node.left:  # se tem filho à esquerda
            hleft = self.height(node.left)
        if node.right:  # se tem filho à direita
            hright = self.height(node.right)
        if hright > hleft:  # se a altura da direita é maior que a altura da esquerda
            return hright + 1  # retorne a altura da direita + 1
        return hleft + 1  # retorne a altura da esquerda + 1


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        """
        Faz a inserção de um nó em uma árvore binária de busca.
        :param value: valor a ser inserido.
        :return: None
        """
        parent = None  # determina o pai do novo nó a ser inserido
        x = self.root  # x começa na raiz
        while x is not None:  # enquanto x diferente de vazio
            parent = x
            if value < x.data:  # se o valor informado é menor que x
                x = x.left  # desça pela direita
            else:  # se não
                x = x.right  # desça pela esquerda
        if parent is None:  # se não tinha nada na árvore (sem raíz)
            self.root = TreeNode(value)  # defina uma nova raíz
        elif value < parent.data:  # se o valor é menor que o parent
            parent.left = TreeNode(value)  # insira o nó à esquerda do parent
        else:  # se não
            parent.right = TreeNode(value)  # insira o nó à direita do parent

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        """
        Faz a busca de um elemento na árvore binária de busca.
        :param value: valor a ser encontrado.
        :param node: nó de referência inicial.
        :return: sub-àrvore iniciando pelo nó.
        """
        if node == 0:  # Se não passamos nenhum nó
            node = self.root  # o nó é a raíz da árvore
        if node is None:  # se o nó for vazio ou
            return None  # retorne vazio
        if node.data == value:  # se o valor do nó for o valor que estou proucurando
            return BinarySearchTree(node)  # retorne uma sub-árvore binária de busca iniciando pelo nó
        if value < node.data:  # se o valor é menor que o nó
            return self._search(value, node.left)  # desça pela esquerda
        return self._search(value, node.right)  # desça pela direita


if __name__ == '__main__':
    tree = BinaryTree(7)
    tree.root.left = TreeNode(18)  # Filho de 7
    tree.root.right = TreeNode(14)  # Filho de 7
    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)
    seed(77)  # especificando a semente
    values = sample(range(1, 1000), 42)
    bst = BinarySearchTree()
    for v in values:
        bst.insert(v)
    print(bst.infixo)

    itens = (1, 3, 981, 510, 1000)
    print()
    for item in itens:
        r = bst.search(item)
        if r is None:
            print(item, 'não encontrado')
        else:
            print(item, 'encontrado')