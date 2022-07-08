class Node:
    # here we will add the constructor
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # and the string method

    def __str__(self):
        return f"{self.data}"


class BinaryTree:
    # the tree will start out empty, with a null head
    def __init__(self):
        self.root = None

    def insert(self, data):
        '''
        Insert(data: any) -> None:\n 
        creates a new Node from the data passed in and adds it to the tree
        If the data is already in the tree, does not insert it again
        '''
        # create a new node frok the data passed in
        new_node = Node(data)
        # if the root doesnt exist set the new node to be the root
        if not self.root:
            self.root = new_node
            return
        # loop over the tree starting and the root
        current_node = self.root
        while current_node:
            # if the data is smaller than the left
            if data < current_node.data:
                if not current_node.left:
                    # set the data to be the left node
                    current_node.left = new_node
                    return
                # ... otherwise set current_node to be left
                else:
                    current_node = current_node.left
            # if the data is bigger than the left
            elif data > current_node.data:
                # ... and if there is not right node
                if not current_node.right:
                    # insert new node to the right
                    current_node.right = new_node
                    return
                # otherwise, a right exists, so the right becomes the current node
                else:
                    current_node = current_node.right
            # the data is a duplicate
            else:
                return

    def search(self, val):
        '''
        search(value: any) -> value or bool:\n 
        Performs depth first search
        Search the Tree for a node with the given value
        If the node exists, return it
        If the node doesn't exist, return false
        '''
        # if there is no root return false
        if not self.root:
            return False

        # loop through the tree starting with the root
        current_node = self.root
        while current_node:
            # if the value is smaller than the current nodes data
            if val < current_node.data:
                current_node = current_node.left
            elif val > current_node.data:
                 # move to the right
                 current_node = current_node.right
            else:
                # this means they are equal
                return current_node

        # return False -- not found
        return False

    def print(self, node=None):
        '''
        print(node=optional: Node) -> None:\n
        prints out all values recursively (in a depth first search fashion)
        defualt start is at root node
        '''
        if not node:
            node = self.root

        # print the node
        print(node)
        # if there is a left node, recursively invoke
        if node.left:
            self.print(node.left)
        # if there is right node recursively invoke
        if node.right:
            self.print(node.right)

    def size(self, node=None):
        '''
        size(node=optional: Node) -> int:\n 
        performs breadth first search
        Calculate the number of nodes in the tree, starting from the given node
        If no node is provided, we can use the root as a sensible default
        '''
        # if no node is passed in, default to using the root
        if not node:
            node = self.root
        count = 0
        def recursive_count(node):
            nonlocal count
            # if not is not none, increase count and recurse on left and right
            if node:
                count += 1
                recursive_count(node.left)
                recursive_count(node.right)
        recursive_count(node)
        return count
        # current_node = self.root
        # while current_node:
        #     if current_node.left:
        #         current_node = current_node.left
        #         count += 1
        #         return
        #     if current_node.right:
        #         current_node = current_node.right
        #         count += 1
        #         return
        #     return count

    def height(self, node=None):
        '''
        height(node=optional: Node) -> int:\n 
        perform breadth first search
        Calculate the maximum amount of nodes in any one path from the given node
        If not given a specific node, default to using the root node
        '''
        # if no node is passed in, default to using the root
        if not node:
            node = self.root
        max_height = 0

        def recurse_height(node, height):
            nonlocal max_height
            if node:
                 # check if height is greater than the max
                if height > max_height:
                    # if so, set the max
                    max_height = height
                # recursively invoke on the left and right nodes
                recurse_height(node.left, height + 1)
                recurse_height(node.right, height + 1)
        recurse_height(node, 1)
        return max_height
        # count = 0
        # def recursive_count(node):
        #     nonlocal count
        #     # if not is not none, increase count and recurse on left and right
        #     if node:
        #         count += 1
        #         recursive_count(node.left)
        #         recursive_count(node.right)
        # recursive_count(node)
    
    def get_max(self):
        '''
        getMax() -> int:\n 
        perform depth first search
        Calculate the maximum value held in the tree
        '''
        # if the tree is empty, return false

        # setthe current  node to be the root and loop over the tree
            # set the current node to be the right
        # if there is no root return false
        if not self.root:
            return False

         # loop through the tree starting with the root
        # current_node = self.root
        # while current_node:
        #     if val > current_node.data:
        #         current_node = current_node.right
        #         if current_node.right > current_node:
        #             return current_node.right
        #     elif val < current_node.data:
        #         return current_node

        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node

        # while current_node:
        #     if current_node.right:
        #         current_node = current_node.right
        #         if not current_node.right:
        #             max = current_node
        #             return max

    def get_min(self):
        '''
        getMin() -> int:\n 
        perform depth first search
        Calculate the minimum value held in the tree
        '''
        if not self.root:
            return False
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node
