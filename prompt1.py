# -*- encoding: utf-8 -*-

'''
    Title: Prompt1

    Description: 

    Goal:
'''


''' The BinaryTree class. '''
class BinaryTree(object):

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

    # Prompt1
    def get_nodes_depth_sum(self, depth=0):

        sum = 0
        if self.left is not None:
            sum += self.left.get_nodes_depth_sum(depth+1) 
        if self.right is not None:
            sum += self.right.get_nodes_depth_sum(depth+1)

        return depth + sum

''' Main. '''
def main():

    b_tree = build_binary_tree()
    
    # Prompt1
    print(b_tree.get_nodes_depth_sum())


def build_binary_tree():

    node_9 = BinaryTree(9)
    node_8 = BinaryTree(8)
    node_7 = BinaryTree(7)
    node_6 = BinaryTree(6)
    node_5 = BinaryTree(5)
    node_4 = BinaryTree(4, node_8, node_9)
    node_3 = BinaryTree(3, node_6, node_7)
    node_2 = BinaryTree(2, node_4, node_5)
    node_1 = BinaryTree(1, node_2, node_3)
    return node_1

if __name__ == '__main__':
    main()