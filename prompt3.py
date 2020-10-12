# -*- encoding: utf-8 -*-

'''
    Title: Prompt3

    Description: 

    Goal:
'''


''' The BinaryTree class. '''
class BinaryTree(object):

    def __init__(self, value, parent=None, left=None, right=None):

        self.value = value
        self.parent = parent
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
 
    # Prompt2
    def get_subtrees_nodes_depth_sum(self):

        sum = self.get_nodes_depth_sum(0)
        if self.left is not None:
            sum += self.left.get_subtrees_nodes_depth_sum()
        if self.right is not None:
            sum += self.right.get_subtrees_nodes_depth_sum()

        return sum

    # Prompt3
    def get_nodes_depth_sum_all(self, caller=None, depth=0):

        sum = 0
        if self.parent is not None and self.parent is not caller:
            sum += self.parent.get_nodes_depth_sum_all(self, depth+1)
        if self.left is not None and self.left is not caller:
            sum += self.left.get_nodes_depth_sum_all(self, depth+1) 
        if self.right is not None and self.right is not caller:
            sum += self.right.get_nodes_depth_sum_all(self, depth+1)

        return depth + sum

''' Main. '''
def main():

    # Return the node you want to calculate for the sum of the distances.
    # This case tries with node_7 by default
    b_tree = build_binary_tree()
    # Prompt3
    print(b_tree.get_nodes_depth_sum_all())


def build_binary_tree():

    node_9 = BinaryTree(9)
    node_8 = BinaryTree(8)
    node_7 = BinaryTree(7)
    node_6 = BinaryTree(6)
    node_5 = BinaryTree(5)
    node_4 = BinaryTree(4, None, node_8, node_9)
    node_3 = BinaryTree(3, None, node_6, node_7)
    node_2 = BinaryTree(2, None, node_4, node_5)
    node_1 = BinaryTree(1, None, node_2, node_3)

    node_9.parent = node_4
    node_8.parent = node_4
    node_7.parent = node_3
    node_6.parent = node_3
    node_5.parent = node_2
    node_4.parent = node_2
    node_3.parent = node_1
    node_2.parent = node_1
    
    return node_7

if __name__ == '__main__':
    main()