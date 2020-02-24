from Tree.tree import BinaryTree, TreeNode

#      '+'
#    /     \
#  'a'     '*'
#         /   \
#       'b'   '-'
#            /    \
#          '/'    'e'
#         /  \
#        'c'  'd'

# (a + (b * ((c/d) - e))
if __name__ == '__main__':
    n1 = TreeNode('a')
    n2 = TreeNode('+')
    n3 = TreeNode('*')
    n4 = TreeNode('b')
    n5 = TreeNode('-')
    n6 = TreeNode('/')
    n7 = TreeNode('c')
    n8 = TreeNode('d')
    n9 = TreeNode('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    tree = BinaryTree()
    tree.root = n2
    tree.simetric_traversal()
