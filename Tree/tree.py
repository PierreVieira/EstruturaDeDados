class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Referência para o nó à esquerda
        self.right = None  # Referência para o nó à direita

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        if data:  # se o usuário especificou o nó
            node = TreeNode(data)
            self.root = node  # Raiz da árvore
        else:
            self.root = None

    def simetric_traversal(self, node=None):
        """Percurso em ordem simétrica"""
        if node is None:  # se o nó é vazio
            node = self.root
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
        # A subarvore da direita só será exibida quando a subarvore da esquerda for exibida


if __name__ == '__main__':
    tree = BinaryTree(7)
    tree.root.left = TreeNode(18)  # Filho de 7
    tree.root.right = TreeNode(14)  # Filho de 7
    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)
