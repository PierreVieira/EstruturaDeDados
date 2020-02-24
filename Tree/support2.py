from Tree.tree import BinaryTree, TreeNode
if __name__ == '__main__':
    tree = BinaryTree()
    n1 = TreeNode('I')
    n2 = TreeNode('N')
    n3 = TreeNode('S')
    n4 = TreeNode('C')
    n5 = TreeNode('R')
    n6 = TreeNode('E')
    n7 = TreeNode('V')
    n8 = TreeNode('A')
    n9 = TreeNode('5')
    n0 = TreeNode('3')
    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    tree.postorder_traversal()
    print(f'Altura: {tree.height()}')