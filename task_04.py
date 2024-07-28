import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Initializing left child
        self.right = None  # Initializing right child
        self.val = key  # Setting the value of the node
        self.color = color  # Additional argument to store the color of the node
        self.id = str(uuid.uuid4())  # Generating a unique identifier for each node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Adding the node to the graph
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Adding edge to the left child
            l = x - 1 / 2 ** layer  # Calculating position for the left child
            pos[node.left.id] = (l, y - 1)  # Setting position for the left child
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Recursively adding edges for the left child
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Adding edge to the right child
            r = x + 1 / 2 ** layer  # Calculating position for the right child
            pos[node.right.id] = (r, y - 1)  # Setting position for the right child
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Recursively adding edges for the right child
    return graph  # Returning the updated graph

def draw_tree(tree_root):
    tree = nx.DiGraph()  # Creating a directed graph
    pos = {tree_root.id: (0, 0)}  # Initializing the position for the root node
    tree = add_edges(tree, tree_root, pos)  # Adding edges to the graph

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Extracting colors of the nodes
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Using node values as labels

    plt.figure(figsize=(8, 5))  # Setting the figure size for the plot
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Drawing the tree
    plt.show()  # Displaying the plot


# Creating a binary heap from a list
def list_to_binary_heap(lst):
    def create_node(index):
        if index >= len(lst):
            return None
        node = Node(lst[index])  # Creating a node for the current index
        node.left = create_node(2 * index + 1)  # Creating the left child
        node.right = create_node(2 * index + 2)  # Creating the right child
        return node

    return create_node(0)  # Returning the root node of the binary heap

# Example list representing a binary heap
heap_list = [1, 3, 5, 7, 9, 2, 6, 8, 4]

# Creating the binary heap from the list
heap_root = list_to_binary_heap(heap_list)

# Displaying the binary heap as a tree
draw_tree(heap_root)
