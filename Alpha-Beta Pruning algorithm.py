# Define a Node class to represent the nodes in the game tree
class Node:
    def __init__(self, value):
        self.value = value  # The value associated with the node
        self.children = []  # List to store the child nodes
    
    def is_terminal(self):
        return not self.children  # Check if the node has no children, indicating a terminal state
    
    def evaluate(self):
        return self.value  # Return the value associated with the node

# Alpha-Beta Pruning algorithm
def alpha_beta(node, depth, alpha, beta, maximizing_player):
    # Base case: if the maximum depth is reached or the node is terminal
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        value = float('-inf')
        # For each child node
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            # If beta becomes less than or equal to alpha, prune the rest of the nodes
            if beta <= alpha:
                break  # Beta cutoff
        return value
    else:
        value = float('inf')
        # For each child node
        for child in node.children:
            value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            # If beta becomes less than or equal to alpha, prune the rest of the nodes
            if beta <= alpha:
                break  # Alpha cutoff
        return value

# Creating a tree structure for demonstration
node6 = Node(6)
node3 = Node(3)
node9 = Node(9)
node5 = Node(5)
node2 = Node(2)
node8 = Node(8)
node1 = Node(1)

# Building the tree structure
node6.children = [node3, node9]
node3.children = [node5, node2]
node9.children = [node8, node1]

# Initial call to alpha_beta function
best_score = alpha_beta(node6, 2, float('-inf'), float('inf'), True)
print(best_score)

#       6
#     /   \
#    3     9
#   / \   / \
#  5   2 8   1
